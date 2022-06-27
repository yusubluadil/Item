from asyncore import read

from django.http import QueryDict
from account.models import User
from courses.models import Course, Header, Video, CourseStudent
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "is_superuser"]


class CourseSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        read_only = True,
        view_name = 'user_detail'
    )
    
    author_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(), source = "author", write_only = True
    )
    
    class Meta:
        model = Course
        fields = "__all__"


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class CourseStudentSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField(read_only = True)
    course_id = serializers.PrimaryKeyRelatedField(
        queryset = Course.objects.all(), source = "course"
    )
    
    student = serializers.StringRelatedField(read_only = True)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(), source = "student"
    )
    
    class Meta:
        model = CourseStudent
        fields = "__all__"