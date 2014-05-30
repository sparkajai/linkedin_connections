from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Register(AbstractUser):
	"""User Register Model"""
	full_name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.full_name

class LinkedinProfileData(models.Model):
	user_id = models.CharField(max_length=30,unique=True)
	email = models.CharField(max_length=30)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	picture_url = models.TextField()

class LinkedinUserFriendsData(models.Model):
	linkedin_profile = models.ForeignKey(LinkedinProfileData)
	full_name = models.CharField(max_length=255)
	photo_url = models.TextField()
