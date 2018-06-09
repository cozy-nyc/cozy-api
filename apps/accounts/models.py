from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
 



class Profile(models.Model):
    """
        This is a model for user's profile.

        Attributes:
            user: The user related to the profile.
            clan: The clan the user is in.
            profileImg: The user's profile image.
            location: Optional location text field.
            name: A property that holds reference the django user's name
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileImg = models.ImageField(upload_to='images/')
    location = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username 

    @property
    def name(self):
        return self.user.username
    
    @property
    def image(self):
        return self.profileImg.image



@receiver(post_save, sender = User)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
    