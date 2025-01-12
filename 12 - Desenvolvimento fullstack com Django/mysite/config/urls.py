from config.admin import admin_site
from django.urls import include, path

urlpatterns = [
    path("admin/", admin_site.urls),
    path("polls/", include("polls.urls")),
    path("contacts/", include("contacts.urls")),
    path("accounts/", include("accounts.urls")),
]
