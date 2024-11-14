from django.urls import path, include
from . import views

app_name = 'facultyapp'
urlpatterns = [
    path('FacultyHomePage/', views.FacultyHomePage, name="FacultyHomePage"),
    path('add_student/', views.add_student, name='add_student'),
    path('add_course/', views.add_course, name='add_course'),
    path('student_list/', views.student_list, name='student_list'),
    path('post_marks/', views.post_marks, name='post_marks'),

]