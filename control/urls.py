from django.urls import path

from products import views
from order import views
# from .views import show
from . import views
app_name = 'products'
urlpatterns = [
    path('',views.show,name="show"),
    path('',views.products,name="products"),

]
    