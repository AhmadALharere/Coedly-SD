#from django.shortcuts import render,redirect
from .models import channel,insights
#from django.urls import reverse
from .serializers import channelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from datetime import timedelta
from django.utils import timezone
from django.db.models import Q

# Create your views here.

class Show_channel_Detail(APIView):
    def get(self,request,id):
        channel_info = channel.objects.get(id=id)
        insights.objects.create(channel=channel_info,account=request.user,action_Type='Reach')
        serializer = channelSerializer(channel_info)
        return Response(serializer.data,status=status.HTTP_200_OK)

    


def Show_channel_insights(request,id):
    wanted_channel = channel.objects.get(id=id)
    now = timezone.now()
    time_limit = now - timedelta(days=30)
    timefilter = Q(action_Date__gte = time_limit)
    reachfilter = Q(action_Type = 'Reach')
    followfilter = Q(action_Type = 'Follow')
    unfollowfilter = Q(action_Type = 'Unfollow')
    channelfilter = Q(channel=wanted_channel)
    reachtime = insights.objects.Value('account').distinct().filter(timefilter & reachfilter & channelfilter).length()
    netfollows = insights.objects.Value('account').distinct().filter(timefilter & followfilter & channelfilter).length()-insights.objects.Value('account').distinct().filter(timefilter & unfollowfilter & channelfilter).length()
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

