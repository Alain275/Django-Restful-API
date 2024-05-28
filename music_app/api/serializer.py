from rest_framework import serializers
from .models import Room  # Import your Room model

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("id","code","host","guest_can_pause","votes_to_skip","created_at") # Include all fields from the Room model
