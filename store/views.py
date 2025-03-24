from django.shortcuts import render , reverse ,redirect
from .models import Slide,Products,Comment,CartItem
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect,Http404


def store(request):
    slides = Slide.objects.all()
    products = Products.objects.all()
    product_id = request.GET.get('product')
    
    if product_id:
            product = Products.objects.get(pk=product_id)
            cart_item = CartItem.objects.filter(product=product)
            if not cart_item:
                cart_item = CartItem.objects.create(customer=request.user, product=product, quantity=1)
                cart_item.save()
                return redirect('store:store')
            for item in cart_item:
                item.quantity += 1
                item.save()


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




def cart(request):
    cart_items = CartItem.objects.filter(customer=request.user)
    print([item.total_price() for item in cart_items])
    total_price = sum([item.total_price() for item in cart_items])
    total_quantity = sum([item.quantity for item in cart_items])

    return render(request, 'cart.html',{'cart_items': cart_items, 'total_quantity': total_quantity, 'total_price': total_price})


def edit_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk)
    action = request.GET.get('action')

    if action == 'take' and cart_item.quantity > 0:
        if cart_item.quantity == 1:
            cart_item.delete()
            return redirect('store:cart')
        cart_item.quantity -= 1
        cart_item.save()
        return redirect('store:cart')
    cart_item.quantity +=1
    cart_item.save()
    return redirect('store:cart')


def delete_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk)
    cart_item.delete()
    return redirect('store:cart')

