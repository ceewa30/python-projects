from django.urls import path
from .views import EmployeeViewSet


urlpatterns = [
    path('curd/', EmployeeViewSet.as_view()),
    path('curd/<int:id>', EmployeeViewSet.as_view())
]