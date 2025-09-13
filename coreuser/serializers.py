from rest_framework import serializers
from .models import CoreUser

class CoreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreUser
        fields ="__all__"
        