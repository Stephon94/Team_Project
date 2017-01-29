from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
	#This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User, related_name="user")

	#The additional attributes we wish to include.
	picture = models.ImageField(upload_to='profile_images', blank=True)
	bio = models.TextField(blank=True)

	def __unicode__(self):
		return self.user.username

# class Category(models.Model):
# 	user = models.ForeignKey(User)
# 	name = models.CharField(max_length=128, unique=True)
# 	likes = models.IntegerField(default=0)
# 	slug = models.SlugField()

	

class ClothingType(models.Model):
	user = models.ForeignKey(User)
	price = models.IntegerField(default=0)
	picture = models.ImageField()
	purchased_at = models.DateTimeField(auto_now=True)
class Size(models.Model):
	name = models.CharField(max_length=128, unique=True)

class Color(models.Model):
	name = models.CharField(max_length=128, unique=True)

class Season(models.Model):
	name = models.ForeignKey(ClothingType)
# class Accessory(models.Model):
# 	user = models.ForeignKey(User)
# 	category = models.ForeignKey(Category)
# 	earrings = models.ImageField(auto_now=True)
# 	necklace = models.ImageField(auto_now=True)
# 	glasses = models.ImageField(auto_now=True)
# 	rings = models.ImageField(auto_now=True)
# 	scarf = models.ImageField(auto_now=True)
# 	hat = models.ImageField(auto_now=True)
# 	belt = models.ImageField(auto_now=True)
