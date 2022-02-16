from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Products
from .filters import ProdactFilter
from django.contrib.auth.decorators import login_required
from .form import ProductForm
# Create your views here.

@login_required

def products(request):
    products = Products.objects.all()
    #filters
    myfilter = ProdactFilter(request.GET,queryset=products)
    products = myfilter.qs 

    paginator = Paginator(products,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # add product
    if request.method == 'POST':
        proform = ProductForm(request.POST, request.FILES)
        if proform.is_valid():
            proform.save()
            return redirect(reverse('products:products'))
    else:
        proform = ProductForm()
    ################################################3
    context = {'products':page_obj , 'myfilter':myfilter , 'proform':proform}
    return render(request,'products/pro_list.html',context)


def product_details(request,id):
    product_details=Products.objects.get(id=id)

    context={'products':product_details}
    return render(request,'products/pro_details.html',context)


def update_product(request , id):
    product = Products.objects.get(id = id)
    if request.method =='POST':
        form = ProductForm(request.POST , request.FILES , instance = product)
        if form.is_valid():
            form.save()
            return redirect('products:product_details',id)
    else:
        form = ProductForm(instance = product)
    context = {'form' : form}
    return render(request,'products/edit_pro.html',context)


def delete_product(request , id):
    product = Products.objects.get(id = id)
    product.delete()

    return redirect(reverse('products:products'))

def delete_pause_product(request , id):
    product = Products.objects.get(id = id)
    product.delete()

    return redirect(reverse('products:pause_products'))

def product_hide(request,id):
    product_hide=Products.objects.get(id=id)
    product_hide.hide = True
    product_hide.save()

    return redirect(reverse('products:pause_products'))


#  pause products

def pause_products(request):
    products = Products.objects.all()
    #filters
    myfilter = ProdactFilter(request.GET,queryset=products)
    products = myfilter.qs 

    paginator = Paginator(products,1000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'products':page_obj , 'myfilter':myfilter}
    return render(request,'products/pause_pro_list.html',context)

