from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("cards/", include("cards.urls", namespace="cards")),
]
