from django.urls import path ,include
from . import views

app_name='employees'

urlpatterns = [
        path('', views.employees, name='employees'),
        path('/<int:id>',views.delete_employee,name='delete_employee'),  
        # path('signup', views.signup, name='signup'),
        path('profile/', views.employe, name='employe'),

        path('profile/<int:id>', views.employee, name='employee'),

        path('employee_edit', views.employee_edit, name='employee_edit'),
]