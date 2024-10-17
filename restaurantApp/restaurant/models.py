from django.db import models
from django.contrib.auth.models import User
from image_cropping import ImageRatioField

# Create your models here.

STATUS = (
    (0, "Unavailable"),
    (1 , "Available")
)

class MenuType(models.Model):
    menu_type = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name ='menu_type'
        verbose_name_plural ='menu_types'

    def __str__(self):
        return self.menu_type

class MenuItem(models.Model):
    menu_item = models.CharField(max_length=100)
    menu_type = models.ForeignKey(MenuType, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    menu_image = models.ImageField(upload_to="menu_image/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'menu_item'
        verbose_name_plural = 'menu_items'

    def __str__(self):
        return self.menu_item


class MenuImage(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    menu_image = models.ImageField(upload_to="menu_image/", blank=True, null=False)
    cropping = ImageRatioField('menu_image', '400x400')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.menu_item.menu_item} - {self.menu_image}"


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu_item.menu_item} - {self.quantity}"
