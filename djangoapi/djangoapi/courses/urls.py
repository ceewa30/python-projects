# from django.conf.urls import url
from django.urls import path, include
from .views import (
    CourseViewSet,
)

urlpatterns = [
    path('api', CourseViewSet.as_view()),
]