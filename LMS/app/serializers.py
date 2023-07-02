from rest_framework import serializers
from . import models



class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instructor
        fields = ['id', 'instructor_name', 'instructor_mailid', 'instructor_password', 'instructor_bio', 'instructor_specialization', 'instructor_experience', 'profile_picture']