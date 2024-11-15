
from django.urls import path , include
from . import views


app_name = 'channel'
urlpatterns = [
    path('<int:id>/ins',views.Show_channel_insights,name='Channelinsights'),
    path('<int:id>/follow',views.follow,name='followChannel'),
    path('<int:id>/unfollow',views.unfollow,name='UnfollowChannel'),
    path('<int:id>',views.Show_channel_Detail,name='ChannelDetails'),
    ]


