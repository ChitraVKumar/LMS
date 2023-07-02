from django.urls import path, include
from .views import main
from . import views

urlpatterns = [
    path('', main),
    path('instructor/', views.InstructorList.as_view()),
    path('instructor/<int:pk>/', views.InstructorDetails.as_view()),
]