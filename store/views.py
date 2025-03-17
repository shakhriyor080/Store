from django.shortcuts import render , reverse ,redirect
from .models import Slide,Products,Comment
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect,Http404


def store(request):
    slides = Slide.objects.all()
    products = Products.objects.all()
  
    return render(request, 'store.html', {'slides':slides, 'products':products , } )



def products_detail(request, pk):
    product = Products.objects.get(pk=pk)
    return render(request, 'products_detail.html', {'product': product})


def search_result(request):
    query = request.GET.get('search')
    search_obj = Products.objects.filter(Q(title__icontains=query)|Q(description__icontains=query))
    return render(request,'search.html', {'search_obj':search_obj,
    'query':query})


def leave_comment(request,pk):
    try:
        news = Products.objects.get(pk=pk)
    except:
        raise Http404("sahifa error ")
    
    if request.user.is_authenticated:
        news.comments.create( comment_text = request.POST.get ('comment_text'))
    
    else:
        news.comments.create( comment_text= request.POST.get('comment_text'))
        comment = Comment.objects.all()
    return HttpResponseRedirect(reverse('store:products_detail', args = (news.pk,)))
