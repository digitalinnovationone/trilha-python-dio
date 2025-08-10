from django.urls import path

from . import views

app_name = "contacts"
urlpatterns = [
    path("", views.get_name, name="get_name"),
    path("thanks/<str:name>", views.thanks, name="thanks"),
    path("create/", views.create, name="create"),
]
