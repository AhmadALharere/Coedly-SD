# Generated by Django 3.2.25 on 2024-11-13 16:59

import channel.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('icon', models.ImageField(upload_to=channel.models.pickimage)),
                ('followers', models.IntegerField(default=0)),
                ('description', models.TextField(default='', max_length=800)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('Type', models.CharField(choices=[('public', 'public'), ('private', 'private')], default='private', max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='insights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_Date', models.DateTimeField(auto_now=True)),
                ('action_Type', models.CharField(choices=[('Follow', 'Follow'), ('Unfollow', 'Unfollow'), ('Reach', 'Reach')], default='Reach', max_length=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channel.channel')),
            ],
        ),
        migrations.DeleteModel(
            name='Jobs',
        ),
    ]
