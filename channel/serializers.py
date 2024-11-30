from rest_framework import serializers
from .models import channel,insights

class channelSerializer(serializers.ModelSerializer):
    class Meta:
        model=channel
        fields = "__all__"
        

 