from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    """
        This is a model for user's profile.

        Attributes:
            user: The user related to the profile.
            profileImg: The user's profile image.
            location: Optional location text field.
            bio: Text field for user's biography
    """

    BROOKLYN = 'Brooklyn'
    QUEENS = 'Queens'
    MANHATTAN = 'Manhattan'
    BRONX = 'Bronx'
    STATENISLAND = 'Staten Island'
    GNA = 'Greater NYC Area'
    NOWHERE = 'Nowhere'
    MOON = 'The Moon'

    LOCATIONS = [
        (BROOKLYN, 'Brooklyn'),
        (QUEENS, 'Queens'),
        (MANHATTAN, 'Manhattan'),
        (BRONX, 'Bronx'),
        (STATENISLAND, 'Staten Island'),
        (GNA, 'Greater NYC Area'),
        (NOWHERE, 'Nowhere'),
        (MOON, 'The Moon')
    ]



    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length = 250, blank = True)
    profileImg = models.ImageField(upload_to='images/')
    location = models.CharField(max_length = 25, choices = LOCATIONS, default=NOWHERE)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

    @property
    def username(self):
        return self.user.username

    @property
    def image(self):
        return self.profileImg.image



@receiver(post_save, sender = User)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
