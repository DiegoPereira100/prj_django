from django.urls import path
from . import views

urlpatterns = [
    path('', views.appHome, name="appHome"),
    path('addUser', views.add_user, name="add_user"),
    path('edit/<int:id_user>', views.edit_user, name="edit_user"),
    path('delete/<int:id_user>', views.delete_user, name="delete_user"),
    path('users', views.listUsers, name="list_users"),
    path('addCourse', views.add_course, name="add_course"),
    path('courses', views.listCourses, name="list_courses"),
    path('buy/<int:course_id>/', views.buy_course, name="buy_course"),
    path('sales_report', views.sales_report, name="sales_report"),
]
