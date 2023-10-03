from rest_framework import serializers
from .models import *

class UserConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConnection
        fields = ["connection_id", "to_computer_id"]

class ConnectionManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionManager
        fields = "__all__"

class ConnectionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionRequest
        fields = "__all__"