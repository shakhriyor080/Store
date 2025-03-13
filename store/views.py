from django.shortcuts import render , reverse ,redirect
from .models import Slide,Products


def store(request):
    slides = Slide.objects.all()
    products = Products.objects.all()
  
    return render(request, 'store.html', {'slides':slides, 'products':products , } )



def products_detail(request, pk):
    product = Products.objects.get(pk=pk)
    return render(request, 'products_detail.html', {'product': product})

