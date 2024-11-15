from django.contrib import admin

# Register your models here.

from .models import channel,insights

admin.site.register(channel)

admin.site.register(insights)