from django.urls import path
from . import views
from django.conf import settings

urlpatterns=[
    path('',views.select.as_view(),name='selecturl'),
    path('cart/',views.cart,name='carturl'),
    path('isession/<int:itno>',views.insert_session,name='insertsessionurl'),

]


