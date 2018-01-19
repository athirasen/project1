from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    childid= models.CharField(max_length=15)
    bio = models.TextField(max_length=500, blank=True)
    email = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return str(self.user.username)

class tech(models.Model):
    user=models.ForeignKey(Profile)
    status=models.BooleanField(default=False)
    room=models.CharField(max_length=20, null=True)
    name=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name
        #return str(self.user_name)








@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
