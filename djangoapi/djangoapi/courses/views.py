# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import permissions
# from .models import Course
# from .serializers import CourseSerializer

# # Create your views here.
# class CourseListApiView(APIView):
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticated]

#     # 1. List all
#     def get(self, request, id=None):
#         """
#         List all the Course from given requested user
#         """

#         course = Course.objects.get(id=id)
#         serializer = CourseSerializer(course, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 2. Create

#     def post(self, request, *args, **kwargs):
#         """
#         Create the Course.
#         """

#         data = {
#             'id': request.get('id'),
#             'name': request.data.get('name'),
#             'language': request.data.get('language'),
#             'price': request.data.get('price'),
#             'user': request.user.id
#         }
#         serializer = CourseSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

class CourseViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, id=None):
        if id:
            item = models.Course.objects.get(user = request.user.id)
            serializer = serializers.CourseSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = models.Course.objects.all()
        serializer = serializers.CourseSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = models.Course.objects.get(id=id)
        serializer = serializers.CourseSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = models.Course.objects.filter(id=id)
        print(item)
        item.delete
        return Response({"status": "success", "data": "Item Deleted"})
