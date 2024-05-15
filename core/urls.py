from django.urls import include, path
from django.contrib.auth.views import LogoutView
from . import views
app_name = "core"


urlpatterns = [
    path("", views.home, name="home"),
]
