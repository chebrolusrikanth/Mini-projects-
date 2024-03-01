from . import views
from django.urls import path


urlpatterns=[
    path('',views.insert.as_view(),name='icecreaminsert'),
    path('select/',views.selecticecreams.as_view(),name='selecticecreams')
]