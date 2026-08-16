from rest_framework import serializers
from .models import User, MemberProfile, PartnerPreference
from matching.models import Match


class PartnerPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerPreference
        fields = ['id', 'min_age', 'max_age', 'preferred_genotype', 'preferred_state', 'preferred_marital_status']


class MemberProfileSerializer(serializers.ModelSerializer):
    preferences = PartnerPreferenceSerializer(read_only=True)

    class Meta:
        model = MemberProfile
        fields = [
            'id', 'first_name', 'last_name', 'gender', 'date_of_birth',
            'state_of_origin', 'residence_city', 'genotype', 'marital_status',
            'occupation', 'about_me', 'account_status', 'preferences'
        ]


class MatchSerializer(serializers.ModelSerializer):
    matched_profile = MemberProfileSerializer(read_only=True)

    class Meta:
        model = Match
        fields = ['id', 'matched_profile', 'compatibility_score', 'status', 'created_at']
