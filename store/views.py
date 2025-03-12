from django.shortcuts import render , reverse ,redirect
from .models import Slide,Products,Category1
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import RegisterForm
def store(request):
    categories = Category1.objects.all()
    slides = Slide.objects.all()
    products = Products.objects.all()

    return render(request, 'store.html', {'slides':slides, 'products':products , 'categories': categories} )

def products_detail(request, slug): 
    product = Products.objects.get(slug=slug)
    return render(request, 'products_detail.html', {'product': product})

def category1_detail(request,slug):
    categorysr = Category1.objects.get(slug__iexact=slug)
    postss = Products.objects.order_by()
    return render(request,'category1_detail.html',{'categorysr':categorysr, 'postss':postss })





def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')

    else:
        form = RegisterForm()
    return render(request, 'register.html',{'form':form})
   