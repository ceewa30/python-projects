from django.contrib import admin
from .models import MenuItem, MenuType, MenuImage, CartItem
from image_cropping import ImageCroppingMixin

# Register your models here.

class MenuTypeAdmin(admin.ModelAdmin):
    list_display = ("menu_type", "status")
    list_filter = ("status", )
    search_fields = ("menu_type", )
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("menu_item", "status")
    list_filter = ("status", )
    search_fields = ("menu_item", "description")

class MenuImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("menu_image", "menu_item")
    list_filter = ("menu_image",)
    search_fields = ("menu_image",)


admin.site.register(MenuType, MenuTypeAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuImage, MenuImageAdmin)
admin.site.register(CartItem)