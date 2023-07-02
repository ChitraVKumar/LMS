from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from rest_framework import generics, permissions
from .serializers import InstructorSerializer

# Create your views here.
def main(request):
    return HttpResponse("<h1>Hello</h1>")


# class InstructorList(APIView):
#     def get(self,request):
#         instructors = models.Instructor.objects.all()
#         serializer = InstructorSerializer(instructors, many=True)
#         return Response(serializer.data)

class InstructorList(generics.ListCreateAPIView):
    queryset = models.Instructor.objects.all()
    serializer_class = InstructorSerializer
    permission_classes = [permissions.IsAuthenticated]


class InstructorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Instructor.objects.all()
    serializer_class = InstructorSerializer
    permission_classes = [permissions.IsAuthenticated]
