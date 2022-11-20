from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Product

import datetime

# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')


def brand(request):
    return render(request, 'dashboard/brand.html')


def product(request):
    return render(request, 'dashboard/product.html')


def order(request):
    return render(request, 'dashboard/order.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    days_till_expiry = product.expiry_date - datetime.date.today()
    return render(request, 'dashboard/detail.html', {'product': product, 'expiry': days_till_expiry})


def list_items(request):
    list_of_iterms_exiring_soon=Product.objects.order_by('expiry_date')
    context={
        'list_of_iterms_exiring_soon': list_of_iterms_exiring_soon
    }
    return render(request, 'dashboard/list.html', context)
