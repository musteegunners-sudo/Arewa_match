import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    def __str__(self):
        return self.email


class MemberProfile(models.Model):
    GENDER_CHOICES = [('MALE', 'Male'), ('FEMALE', 'Female')]
    GENOTYPE_CHOICES = [('AA', 'AA'), ('AS', 'AS'), ('SS', 'SS'), ('AC', 'AC')]
    MARITAL_STATUS = [('SINGLE', 'Single'), ('DIVORCED', 'Divorced'), ('WIDOWED', 'Widowed')]
    ACCOUNT_STATUS = [('PENDING', 'Pending'), ('ACTIVE', 'Active'), ('SUSPENDED', 'Suspended')]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    
    # Cultural & Background Information
    state_of_origin = models.CharField(max_length=100, blank=True)
    residence_city = models.CharField(max_length=100, blank=True)
    genotype = models.CharField(max_length=5, choices=GENOTYPE_CHOICES, blank=True)
    marital_status = models.CharField(max_length=15, choices=MARITAL_STATUS, default='SINGLE')
    occupation = models.CharField(max_length=100, blank=True)
    about_me = models.TextField(blank=True)
    
    account_status = models.CharField(max_length=20, choices=ACCOUNT_STATUS, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.gender})"


class PartnerPreference(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.OneToOneField(MemberProfile, on_delete=models.CASCADE, related_name='preferences')
    min_age = models.PositiveIntegerField(default=18)
    max_age = models.PositiveIntegerField(default=60)
    preferred_genotype = models.CharField(max_length=10, blank=True, help_text="e.g., AA, AS acceptable")
    preferred_state = models.CharField(max_length=100, blank=True)
    preferred_marital_status = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Preferences for {self.profile.first_name}"
