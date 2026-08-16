import uuid
from django.db import models
from common.models import MemberProfile

class Match(models.Model):
    STATUS_CHOICES = [
        ('SUGGESTED', 'Suggested'),
        ('LIKED', 'Liked'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_profile = models.ForeignKey(MemberProfile, on_delete=models.CASCADE, related_name='matches_initiated')
    matched_profile = models.ForeignKey(MemberProfile, on_delete=models.CASCADE, related_name='matched_with')
    compatibility_score = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SUGGESTED')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_profile', 'matched_profile')

    def __str__(self):
        return f"{self.user_profile.first_name} <-> {self.matched_profile.first_name} ({self.compatibility_score}%)"
