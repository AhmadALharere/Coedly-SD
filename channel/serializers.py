from rest_framework import serializers
from .models import channel

class channelSerializer(serializers.ModelSerializer):
    class Meta:
        Model=channel
        fields = "__all__"
        
 