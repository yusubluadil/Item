from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreateAPIView.as_view()),
    path('users/<int:pk>', views.UserDetailAPIView.as_view(), name = 'user_detail'),
    
    path('courses/', views.CourseListCreateAPIView.as_view()),
    path('courses/<int:pk>', views.CourseDetailAPIView.as_view()),
    
    path('headers/', views.HeaderListCreateAPIView.as_view()),
    path('headers/<int:pk>', views.HeaderDetailAPIView.as_view()),
    
    path('videos/', views.VideoListCreateAPIView.as_view()),
    path('videos/<int:pk>', views.VideoDetailAPIView.as_view()),
    
    path('course-students/', views.CourseStudentListCreateAPIView.as_view()),
    path('course-students/<int:pk>', views.CourseStudentDetailAPIView.as_view()),
]