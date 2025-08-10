from django.urls import path

from . import views

app_name = "cards"
urlpatterns = [
    path("request-card/", views.request_card, name="request_card"),
    path("my-requests/", views.view_requests, name="view_requests"),
    path("request-details/<int:card_id>/", views.card_details, name="card_details"),
]
