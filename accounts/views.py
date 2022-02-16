from django.contrib.auth import authenticate, login
from django.core.checks import messages
from django.shortcuts import redirect, render
from .forms import SignupForm ,EmployeeForm ,UserForm
from .models import Employee
from django.urls import reverse
from django.core.paginator import Paginator
from .filters import EmployeeFilter
# Create your views here.

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username='username', password='password')
#             return redirect('accounts:signup')
#     else:
#         form = SignupForm()
#     return render(request,'accounts/profile_list.html',{'form':form})



def employee(request,id):
    emp = Employee.objects.get(id = id)
    return render(request, 'accounts/employee.html',{'emp':emp})

def employe(request):
    emp = Employee.objects.get(user=request.user)
    return render(request, 'accounts/employee.html',{'emp':emp})


def employee_edit(request):
    emp = Employee.objects.get(user=request.user)
    if request.method=='POST':
        userform = UserForm(request.POST,instance=request.user)
        employeeform= EmployeeForm(request.POST,request.FILES, instance=emp)
        if userform.is_valid() and employeeform.is_valid():
            userform.save()
            employeeform = employeeform.save(commit=False)
            employeeform.user = request.user
            employeeform.save() 
            return redirect(reverse('accounts:employee',kwargs={"id":emp.id}))
    else:
        userform = UserForm(instance=request.user)
        employeeform = EmployeeForm(instance=emp)
    return render(request, 'accounts/profile_edit.html',{'userform':userform , 'employeeform':employeeform})    


def employees(request):
    employees = Employee.objects.all()
    #filters
    myfilter = EmployeeFilter(request.GET,queryset=employees)
    employees = myfilter.qs 

    paginator = Paginator(employees,7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # add employee
    if request.method == 'POST':
        empform = SignupForm(request.POST)
        if empform.is_valid():
            empform.save()
            username = empform.cleaned_data['username']
            password = empform.cleaned_data['password1']
            user = authenticate(username='username', password='password')
            return redirect('accounts:employees')
    else:
        empform = SignupForm()
    ################################################3
    context = {'employees':page_obj , 'myfilter':myfilter,'empform':empform}
    return render(request,'accounts/profile_list.html',context)


def delete_employee(request , id):
    employee = Employee.objects.get(id = id)
    employee.delete()

    return redirect(reverse('accounts:employees'))
