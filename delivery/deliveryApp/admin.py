from django.contrib import admin
from .models import Manager, Delivery_In,  Client, Delivery_Out, EndClient, Bill

admin.site.register(Manager)
admin.site.register(Delivery_Out)
admin.site.register(Client)
admin.site.register(Delivery_In)
admin.site.register(EndClient)
admin.site.register(Bill)
