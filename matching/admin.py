from django.contrib import admin
from .models import Match

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'matched_profile', 'compatibility_score', 'status', 'created_at')
    list_filter = ('status', 'compatibility_score')
    search_fields = ('user_profile__first_name', 'matched_profile__first_name')
