from django.urls import path
from .  import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('index/', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('menu/', views.MenuListClassView.as_view(), name='menu'),
    path('order/', views.OrderClassView.as_view(), name='order'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:menu_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]