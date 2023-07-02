from django.db import models

# Create your models here.
# Student
class Student(models.Model):
    student_username = models.CharField(max_length=50)
    student_mailid = models.CharField(max_length=50)
    student_password = models.CharField(max_length=50)
    courses = models.TextField()
    student_qualification = models.CharField(max_length=150)  

    class Meta:
        verbose_name = "1. Student" 

# Instructor
class Instructor(models.Model):
    instructor_name = models.CharField(max_length=50)
    instructor_mailid = models.CharField(max_length=50)
    instructor_password = models.CharField(max_length=50)
    instructor_bio = models.TextField()
    instructor_specialization = models.CharField(max_length=150)
    instructor_experience = models.IntegerField()
    profile_picture = models.ImageField(upload_to='instructor_profiles/', null=True, blank=True)

    class Meta:
        verbose_name = "2. Instructor" 

# Course Catalog
class CourseCatalog(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()
    duration = models.IntegerField() 
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "3. Course Catalog" 

# Course
class Course(models.Model):
    course_title = models.CharField(max_length=200)
    course_description = models.TextField()
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    category = models.ForeignKey(CourseCatalog, on_delete=models.CASCADE)
    students = models.ManyToManyField('Student')
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = "4. Course" 