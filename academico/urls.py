from django.urls import path
from . import views

app_name = "academico"
urlpatterns = [
    path("", views.home, name="home"),
    path("add_course/", views.add_course, name="add_course"),
    path("delete_course/<int:id>", views.delete_course, name="delete_course"),
    path("edit_course/<int:id>", views.edit_course, name="edit_course"),
    path("update_course/<int:id>", views.update_course, name="update_course"),
]
