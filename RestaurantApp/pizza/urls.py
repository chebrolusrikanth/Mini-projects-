from . import views
from django.urls import path

urlpatterns=[
    path('',views.insertpizza.as_view(),name='insertpizzaurl'),
    path('select/',views.selectpizza.as_view(),name='selectpizzaurl'),

]