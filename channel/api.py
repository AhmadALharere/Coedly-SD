from .models import channel,insights
from .serializers import channelSerializer
from datetime import timedelta
from django.utils import timezone
from django.db.models import Q
from rest_framework import generics
from django.http import JsonResponse
# Create your views here.

class Show_channel_Detail(generics.RetrieveAPIView):
    queryset = channel
    serializer_class = channelSerializer
    lookup_field = 'id'


def Show_channel_insights(request,id):
    wanted_channel = channel.objects.get(id=id)
    now = timezone.now()
    time_limit = now - timedelta(days=30)
    timefilter = Q(action_Date__gte = time_limit)
    reachfilter = Q(action_Type = 'Reach')
    followfilter = Q(action_Type = 'Follow')
    unfollowfilter = Q(action_Type = 'Unfollow')
    channelfilter = Q(channel=wanted_channel)
    reachtime = insights.objects.filter(account=request.user).filter(timefilter & reachfilter & channelfilter).count()
    netfollows = insights.objects.filter(account=request.user).filter(timefilter & followfilter & channelfilter).count()-insights.objects.values('account').filter(timefilter & unfollowfilter & channelfilter).count()
    resaults = {"netfollow":netfollows,"reachtime":reachtime}
    return JsonResponse(resaults)



def follow(request,id):
    channel_info = channel.objects.get(id=id)
    channel_info.followers+=1
    channel_info.save()
    insights.objects.create(channel=channel_info,account=request.user,action_Type='Follow')
    return JsonResponse({"status":"success","massage":"you now following this channel"})

def unfollow(request,id):
    channel_info = channel.objects.get(id=id)
    channel_info.followers-=1
    channel_info.save()
    insights.objects.create(channel=channel_info,account=request.user,action_Type='Unfollow')
    return JsonResponse({"status":"success","massage":"you now unfollowing this channel"})

