from django.urls import path
from . import views
app_name = 'order'
urlpatterns = [
    path('',views.order,name="order"),
    path('<int:id>',views.order_details,name="order_details"),
    path('/<int:id>',views.order_wait,name="order_wait"),
    path('//<int:id>',views.make_order_done,name='make_order_done'),  
    path('/<int:id>/',views.order_back,name='order_back'),  
    path('/old-order',views.order_done,name='order_done'),  
    path('/old-order/',views.order_done_delete,name='order_done_delete'),  


]
    