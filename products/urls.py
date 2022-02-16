from django.urls import path
from . import views
app_name = 'products'
urlpatterns = [
    path('products',views.products,name="products"),
    path('pause_pro/<int:id>',views.product_hide,name="product_hide"),
    path('pause_pro',views.pause_products,name="pause_products"),
    path('pause_pro/<int:id>/',views.delete_pause_product,name='delete_pause_product'),  
    path('<int:id>/',views.delete_product,name='delete_product'),  
    path('<int:id>',views.product_details,name='product_details'),    
    path('edir_pro/<int:id>',views.update_product,name='update_product'),  
    
]
    