from rest_framework import serializers
from.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Employee
        # fields = ['id', 'username', 'password', 'email']
        fields = '__all__'