from django.shortcuts import render,redirect
from .models import Slide,Products,Category1
from django.http import HttpResponse, HttpResponseRedirect, Http404

def store(request):
    categories = Category1.objects.all()
    slides = Slide.objects.all()
    products = Products.objects.all()

    return render(request, 'store.html', {'slides':slides, 'products':products , 'categories': categories} )

def category1_detail(request,slug):
    categorysr = Category1.objects.get(slug__iexact=slug)
    postss = Products.objects.order_by()
    return render(request,'category1_detail.html',{'categorysr':categorysr, 'postss':postss })
