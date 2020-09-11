from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('customer/<str:pk>/',views.customer,name='customer'),
    path('createOrder/<str:pk>',views.createOrder,name='create_order'),
    path('updateOrder/<str:pk>/',views.updateOrder,name='update_order'),
    path('deleteOrder/<str:pk>/',views.deleteOrder,name='delete_order'),
]
