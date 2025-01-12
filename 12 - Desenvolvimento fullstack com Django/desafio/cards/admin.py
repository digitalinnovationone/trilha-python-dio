from django.contrib import admin

from cards.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("number", "user", "network", "status", "created_at")
    list_filter = ("status", "network", "created_at")
    search_fields = ("user__username", "status")
