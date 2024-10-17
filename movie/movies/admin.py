from django.contrib import admin
from .models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "duration", "rating")
    search_fields = ("name", "duration", "rating")
    list_filter = ("duration", "rating")
    ordering = ("name", "duration", "rating")

admin.site.register(Movie, MovieAdmin)
