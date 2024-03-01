from django.shortcuts import render,redirect
from icecream.models import icecreams
from pizza.models import pizza
from django.urls import reverse
from django.views.generic.list import ListView
# Create your views here.
from django.views import View
from django.shortcuts import HttpResponse
from itertools import chain

class select(View):
    def get(self,request):
        return render(request,'orderingtemps/display.html')
        

def cart(request):
    amount=0
    icecount=0
    pcount=0

    cream=icecreams.objects.filter(ItemNumber__in=request.session['order_cart']).values()
    pcart=pizza.objects.filter(ItemNumber__in=request.session['order_cart']).values()
    icecount=len(cream)
    pcount=len(pcart)

    for i in cream:
        amount=amount+i['price']
    for i in pcart:
        amount=amount+i['price']
    
    pizzacart=pizza.objects.filter(ItemNumber__in=request.session['order_cart'])
    icecreamCart=icecreams.objects.filter(ItemNumber__in=request.session['order_cart'])

    combain_quertset=list(chain(pizzacart,icecreamCart))

    return render(request,'orderingtemps/details.html',{'icecount':icecount,'pizzacount':pcount,'amount':amount,'combain_qset':combain_quertset})

def insert_session(request,itno):
    request.session.modified=True
    if 'order_cart' in request.session:
        request.session['order_cart'].append(itno)
    else:
        request.session['order_cart']=[itno]
        
    return redirect(reverse('carturl',)) 


def delete_sessionitem(request,itno):   
    if 'order_cart' in request.session and itno in request.session['order_cart']:
        request.session['order_cart']=[x for x in request.session['order_cart'] if x!=itno]
                
        return redirect(reverse('carturl'))     
            
    return HttpResponse('item not found')
    
