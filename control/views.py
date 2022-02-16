from django.urls import reverse

from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required

from accounts.models import Employee
from products.views import products
from accounts.views import employees

# Create your views here.
@login_required
def show(request):
    emp = Employee.objects.get(user=request.user)
    if emp.user.is_superuser :
        return redirect(reverse('products:products'))
    else:
        return redirect(reverse('order:order'))

