from django.shortcuts import render, get_object_or_404
from .models import *

def home(request):
    products = Product.objects.all()
    
    if request.method == 'POST':
        customer = request.user.customer
        product = get_object_or_404(Product, pk=product_id)

        obj, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, new =  Item.objects.get_or_create(order=obj, product=product)
        orderItem.quantity  = orderItem.quantity + 1
        orderItem.save()

    context = {
        'products': products
    }
    return render(request, 'home.html', context)


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'product.html', context)

def checkout(request):
    return render(request, 'checkout.html')

def cart(request):
    orderItems = Item.objects.all()
    context = {
        'orderItems': orderItems
    }
    return render(request, 'cart.html', context)


    