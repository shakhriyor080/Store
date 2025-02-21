from django.shortcuts import render,redirect
from .models import Slide,Products


def store(request):
    slides = Slide.objects.all()
    products = Products.objects.all()
    return render(request, 'store.html', {'slides':slides, 'products':products} )