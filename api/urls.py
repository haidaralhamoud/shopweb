from django.urls import path
from . import views
urlpatterns = [
    path('',views.apiAll,name="apiAll"),
    
    path('products/',views.productsList,name="products"),
    path('order/',views.orderList,name="order"),
    path('create_order/',views.orderCreate.as_view(),name="create_order"),

    path('products_delail/<str:pk>/',views.productsDelail,name="products_delail"),

    path('create_products/',views.productsCreate.as_view(),name="create_products"),

    path('update_products/<str:pk>/',views.productsUpdate,name="update_products"),

    path('delete_products/<str:pk>/',views.productsDelete,name="delete_products"),
]
