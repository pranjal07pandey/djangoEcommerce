from django.shortcuts import render, redirect
from .models import *
from .forms import ProductForm
from django.db.models import Q



# Create your views here.
def store(request):
    products = Product.objects.all()

    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(name__startswith = query)
        )


    return render(request, 'store/store.html', {
        'products':products
    })

def addProducts(request):
    form = ProductForm()

    if request.method =='POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('store')
    
    return render(request, 'store/addProducts.html',{
        'form': form
    })

def viewProduct(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'store/product.html',{
        'product': product
    })


def cart(request):

    cusotmer = request.user.id
    print(cusotmer)
    order, created = Order.objects.get_or_create(user = cusotmer, complete= False)
    items = order.orderitem_set.all()

    return render(request, 'store/cart.html',{
        'items':items,
        'order':order
    })

def checkout(request):

    cusotmer = request.user.id
    order, created = Order.objects.get_or_create(user = cusotmer, complete= False)
    items = order.orderitem_set.all()

    return render(request, 'store/checkout.html',{
         'items':items,
        'order':order
    })
