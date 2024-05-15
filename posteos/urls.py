from django.urls import path, include
from . import views

app_name = "posteos"



urlpatterns = [
    path("", views.posteo_list, name="home"),
    path("posteo/detail/<int:pk>", views.PosteoDetail.as_view(), name="posteo_detail"),
    path("posteo/create", views.NuevoPostView.as_view(), name="posteo_create"),
]