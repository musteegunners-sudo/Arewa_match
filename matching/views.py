from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common.models import MemberProfile
from common.serializers import MatchSerializer
from .models import Match
from .services import generate_matches_for_user


class SuggestedMatchesView(APIView):
    def get(self, request, profile_id):
        try:
            profile = MemberProfile.objects.get(id=profile_id)
        except MemberProfile.DoesNotExist:
            return Response({"error": "Member profile not found"}, status=status.HTTP_404_NOT_FOUND)

        # Generate new matches based on current algorithm
        generate_matches_for_user(profile)

        # Retrieve all calculated matches sorted by compatibility
        matches = Match.objects.filter(user_profile=profile).order_by('-compatibility_score')
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
