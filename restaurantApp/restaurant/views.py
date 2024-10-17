from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem, MenuType, CartItem
from django.views.generic import ListView, TemplateView

# Create your views here.
# def MenuList(request):
#     menu_items = MenuItem.objects.all()
#     menu_types = MenuType.objects.all()
#     template_name = "menu.html"
#     context = {
#         "menu_items": menu_items,
#         "menu_types": menu_types,
#         }
#     return render(request, template_name, context)

class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = "about.html"

class MenuListClassView(ListView):
    model = MenuItem
    template_name = "menu.html"
    context_object_name = 'menu_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_types'] = MenuType.objects.all()
        return context

class OrderClassView(ListView):
    model = MenuItem
    template_name = "order.html"
    context_object_name = 'menu_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_types'] = MenuType.objects.all()
        return context

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.menu_item.price * item.quantity for item in cart_items)
    return render(request, "view_cart.html", {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, menu_id):
    menu_item = MenuItem.object.get(id=menu_id)
    cart_item, created = CartItem.objects.get_or_create(menu_item=menu_item, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('restaurant:view_cart')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('restaurant:view_cart')
