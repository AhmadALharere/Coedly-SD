from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

channel_type = (('public','public'),('private','private'))
Action_Type = (('Follow','Follow'),('Unfollow','Unfollow'),('Reach','Reach'))

def pickimage(instance,filename):
    name , extention = filename.split('.')
    return "channel/icons/%s.%s"%(instance.id,extention)

class channel(models.Model):

    name = models.CharField(default='',max_length=100)
    icon = models.ImageField(upload_to=pickimage)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    followers = models.IntegerField(default=0)
    description = models.TextField(default='',max_length=800)
    created_on = models.DateTimeField(auto_now=True)
    Type = models.CharField(default='private', max_length=50,choices=channel_type)
    
    def __str__(self):
        return self.name

 
    
class insights(models.Model):
    
    channel = models.ForeignKey('channel', on_delete=models.CASCADE)
    account = models.ForeignKey(User, on_delete=models.CASCADE) 
    action_Date = models.DateTimeField(auto_now=True)
    action_Type = models.CharField(default='Reach',max_length=10,choices=Action_Type)
           