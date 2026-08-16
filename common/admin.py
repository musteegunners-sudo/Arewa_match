from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, MemberProfile, PartnerPreference


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'phone_number', 'is_verified', 'is_staff', 'created_at')
    list_filter = ('is_verified', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username', 'phone_number')
    ordering = ('-created_at',)


class PartnerPreferenceInline(admin.StackedInline):
    model = PartnerPreference
    extra = 0


@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'state_of_origin', 'account_status', 'created_at')
    list_filter = ('gender', 'account_status', 'marital_status', 'genotype')
    search_fields = ('first_name', 'last_name', 'user__email', 'state_of_origin')
    inlines = [PartnerPreferenceInline]


@admin.register(PartnerPreference)
class PartnerPreferenceAdmin(admin.ModelAdmin):
    list_display = ('profile', 'min_age', 'max_age', 'preferred_genotype', 'preferred_state')
