from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
        This is a model for user's profile.

        Attributes:
            user: The user related to the profile.
            clan: The clan the user is in.
            profileImg: The user's profile image.
            location: Optional location text field.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clan = models.ForeignKey(Clan , on_delete=models.CASCADE)
    profileImg = models.ForeignKey(ProfileImg , on_delete=models.CASCADE)
    location = models.TextField(max_length=50, blank=True)

    def __unicode__(self):
        return self.user.username



class Clan(models.Model):
    """
        This is a model for Clans. As of now all Clains are animals.

        Attributes:
            CLAN: Cats, Dogs, Birds, Pigeons, Rats, Racoons, Repitles, Snakes
    """
    CLAN = (
        (CATS, 'Cats'),
        (DOGS, 'Dogs'),
        (RATS, 'Rats'),
        (RACCONS, 'Racoons'),
        (BIRDS, 'Birds'),
        (PIGEONS, 'Pigeons'),
        (REPTILES,'Reptiles'),
        (SNAKES, 'Snakes'),
    )

    def __str__(self):
        return self.CLAN

class ProfileImg(models.Model):
    """
        This is a model for Profile images. The options of images are tied to the
            parent Clan.

        Attributes:
            parent: The related Clan.
            image: A profile image.
    """
    parent = models.ForeignKey(Clan, related_name = 'profileImg', on_delete=models.CASCADE)
    image = models.ImageField()
