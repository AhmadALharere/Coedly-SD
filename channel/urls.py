
from django.urls import path 
from . import api


app_name = 'channel'
urlpatterns = [
    path('<int:id>/ins',api.Show_channel_insights,name='Channelinsights'),
    path('<int:id>/follow',api.follow,name='followChannel'),
    path('<int:id>/unfollow',api.unfollow,name='UnfollowChannel'),
    path('<int:id>',api.Show_channel_Detail.as_view(),name='ChannelDetails'),
    ]


