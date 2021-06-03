from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
# Create your models here.


User = settings.AUTH_USER_MODEL

class FollowerRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=220, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) #most recent time profile was saved
    followers = models.ManyToManyField(User, related_name='following', blank=True)




    """
    profile_obj = profile.objects.first()
    profile_obj.followers.all() -> All users following this profile
    user.following.all() -> All users I follow
    """

def user_did_save(sender, instance, created, *args, **kwargs): #postsave lets you define user_did_save, arbitrary name, for post_save arguements are sender, instance, and created
    if created:    #if created, 
        Profile.objects.get_or_create(user=instance) #create profile for user

post_save.connect(user_did_save, sender=User) #in order to use user_did_save we must connect it to post_save, after user is saved, the receiver function "user_did_save" will trigger

