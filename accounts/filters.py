import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    fname = django_filters.CharFilter(lookup_expr='icontains')
    #description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Employee
        fields = ('fname','city')

