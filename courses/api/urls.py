from django.urls import path

from . import views


app_name = 'courses'

urlpatterns = [
    path('subjects/', views.SubjectList.as_view(), name='subject_list'),
    path('subjects/<pk>/', views.SubjectDetail.as_view(), name='subject_detail'),
    path('subjects/<pk>/enroll/', views.CourseEnrollView.as_view(), name='course_enroll'),
]
