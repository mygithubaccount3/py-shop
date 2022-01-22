from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Offer


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def news(request):
    return HttpResponse('Here is a page for new products')


def offers(request):
    offers_data = Offer.objects.all()
    return render(request, 'offers.html', {'offers': offers_data})
