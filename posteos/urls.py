from django.urls import path, include
from . import views

app_name = "posteos"



urlpatterns = [
    path("", views.posteo_list, name="home"),
    path("posteos/detail/<int:pk>", views.PosteoDetail.as_view(), name="posteo_detail"),
    path("posteos/create", views.NuevoPostView.as_view(), name="posteo_create"),
    path("posteos/buscar", views.buscar_posts, name="posteo_buscar"),
    path('<int:posteo_id>/confirmar-eliminacion/', views.confirmar_eliminacion, name='confirmar_eliminacion'),
    path('<int:posteo_id>/borrar/', views.borrar_posteo, name='borrar_posteo'),
]