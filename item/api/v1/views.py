from rest_framework.response import Response
from account.models import User
from courses.models import Course, Header, Video, CourseStudent
from .serializers import UserSerializer, CourseSerializer, HeaderSerializer, VideoSerializer, CourseStudentSerializer
from rest_framework import generics

""" My user views """
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


""" My course views """
class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


""" My header views """
class HeaderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer

class HeaderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer


""" My video views """
class VideoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


""" My coursestudent views """
class CourseStudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = CourseStudent.objects.all()
    serializer_class = CourseStudentSerializer

class CourseStudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseStudent.objects.all()
    serializer_class = CourseStudentSerializer