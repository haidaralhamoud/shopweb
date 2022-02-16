from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Order
from .form import ProductForm
from .filters import OrderFilter
from django.core.paginator import Paginator

# Create your views here.


def order(request):
    orders = Order.objects.all()

    if request.method == 'POST':
        proform = ProductForm(request.POST, request.FILES)
        if proform.is_valid():
            proform.save()
            return redirect(reverse('order:order'))
    else:
        proform = ProductForm()

    context = { 'orders':orders, 'proform':proform}
    return render(request,'order/order_list.html',context)


def order_details(request,id):
    orders = Order.objects.get(id=id)
    order = orders.products.all()
    # orders.products.id = orders.id_products
    context = { 'orders':orders ,'order':order} 
    return render(request,'order/order_details.html',context)

def order_wait(request,id):

    order_wait=Order.objects.get(id=id)
    order_wait.receive = 2
    order_wait.user = request.user.username
    order_wait.save()

    return redirect(reverse('order:order'))

def make_order_done(request,id):

    order_done=Order.objects.get(id=id)
    order_done.done = 1
    order_done.save()

    return redirect(reverse('order:order'))

def order_done(request):
    order_done = Order.objects.all()
    #filters
    myfilter = OrderFilter(request.GET,queryset=order_done)
    order_done = myfilter.qs 

    paginator = Paginator(order_done,7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'order_done':page_obj , 'myfilter':myfilter }
    return render(request,'order/order_done.html',context)

def order_done_delete(request):
    order_done = Order.objects.all()
    for order in order_done:
        if order.done == 1:
            order.delete()
    return redirect(reverse('order:order_done'))


def order_back(request,id):

    order_back=Order.objects.get(id=id)
    order_back.receive = 1
    order_back.user = 'admin'
    order_back.save()

    return redirect(reverse('order:order'))
