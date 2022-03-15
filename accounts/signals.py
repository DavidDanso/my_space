from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import *

def create_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='user')
		instance.groups.add(group)
		Person.objects.create(user=instance, username=instance.username, email=instance.email)
		print('Profile created!')

post_save.connect(create_profile, sender=User)