from django.contrib import admin
from django.urls import path
from matching.views import SuggestedMatchesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/matches/<uuid:profile_id>/', SuggestedMatchesView.as_view(), name='suggested-matches'),
]

