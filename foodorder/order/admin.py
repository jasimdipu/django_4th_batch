from django.contrib import admin
from .models import Customer, Product, Order


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['email', "phone"]
    list_filter = ['phone', 'name']
    list_display = ['name', 'email', 'phone']
    list_per_page = 10


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', "category"]
    list_filter = ['date_created', 'price']
    list_display = ['name', 'category', 'price']
    list_per_page = 10


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
