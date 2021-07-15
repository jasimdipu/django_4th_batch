from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name


# select * from customer where name='john doe';

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    category = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=200, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    Status = (
        ("Pending", 'Pending'),
        ("Delivered", 'Delivered'),
        ("Out of delivery", 'Out of delivery'),
    )
    customer_id = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product_id = models.ManyToManyField(Product, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=Status)

    def __str__(self):
        return self.customer_id.name + " "+ self.customer_id.email
