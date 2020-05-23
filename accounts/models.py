# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
	phone = models.CharField(max_length=11)
	address = models.CharField(max_length=255)
	town = models.CharField(max_length=45)
	postcode = models.CharField(max_length=45)
	country = models.CharField(max_length=45)

	class Meta:
		verbose_name_plural = 'User Details'

	def __str__(self):
		return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
