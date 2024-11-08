from django.urls import path
from . import views

urlpatterns = [
    path('', views.appHome, name="appHome"),
    path('add', views.add_user, name="add_user"),
    path('users', views.listUsers, name="list_users"),
]
