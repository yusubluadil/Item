from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField(default=0)
    rating = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    update_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title

class Header(models.Model):
    title = models.CharField(max_length=100)
    course = models.OneToOneField(Course, models.CASCADE)
    
    def __str__(self):
        return self.title

class Video(models.Model):
    video_name = models.CharField(max_length=100)
    video = models.FileField()
    video_header = models.ForeignKey(Header, on_delete=models.CASCADE, related_name='videos')
    
    def __str__(self):
        return self.video_name

class CourseStudent(models.Model):
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE, related_name='course_students') # yazilisa diqqet
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_students')