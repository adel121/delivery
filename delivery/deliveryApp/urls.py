from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns=[
path('bill_details/<int:bill_id>/', views.bill_details,name='bill_details'),
path('bill_details/<int:bill_id>/<str:status>/', views.bill_details,name='bill_details'),
path('bills/',views.index,name='index'),
path('bills/<str:category>/',views.index,name='index'),
path('bills/<str:category>/<int:year>/<int:month>/<int:day>',views.index,name='index'),
path('bills/<int:year>/<int:month>/<int:day>/',views.index,name='index'),
path('add_endclient',views.add_endclient,name='add_endclient'),
path('add_manager',views.add_manager,name='add_manager'),
path('add_deliveryout',views.add_deliveryout,name='add_deliveryout'),
path('add_client',views.add_client,name='add_client'),
path('add_deliveryin',views.add_deliveryin,name='add_deliveryin'),
path('add_bill',views.add_bill,name='add_bill'),
]