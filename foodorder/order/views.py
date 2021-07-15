from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm


# Create your views here.


def index(request):
    products = Product.objects.all()
    cursor = {"products": products}
    return render(request, "index.html", cursor)


def products(request):
    return render(request, "products.html")


def order_list(request, pk):
    order = Order.objects.get(id=pk)
    # product = order.product_id.name
    cursor = {"order": order}
    return render(request, "order_list.html", cursor)


def createOrderForm(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, 'order_form.html', context)


def updateOder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, 'order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {"item": order}
    return render(request, 'delete.html', context)
