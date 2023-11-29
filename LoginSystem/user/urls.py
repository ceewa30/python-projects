from django.urls import path, include
# from django.conf import settings
from . import views
# from django.conf.urls.static import static
 
urlpatterns = [
        path('', views.index, name='home'),
        path('login/', views.user_login, name='login'),
        path('signup/', views.user_signup, name='signup'),
        path('logout/', views.user_logout, name='logout'),
]
