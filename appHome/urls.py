from django.urls import path
from . import views

urlpatterns = [
    path('', views.appHome, name="appHome"),
    path('addUser', views.add_user, name="add_user"),
    path('users', views.listUsers, name="list_users"),
    path('addCourse', views.add_course, name="add_course"),
    path('courses', views.listCourses, name="list_courses"),
]
