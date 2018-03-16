from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
 
 
class Clan(models.Model):
    """
        This is a model for Clans. As of now all Clains are animals.

        Attributes:
            CLAN: Cats, Dogs, Birds, Pigeons, Rats, Racoons, Repitles, Snakes
    """
    CLAN = (
        ('CATS', 'Cats'),
        ('DOGS', 'Dogs'),
        ('RATS', 'Rats'),
        ('RACCONS', 'Racoons'),
        ('BIRDS', 'Birds'),
        ('PIGEONS', 'Pigeons'),
        ('REPTILES','Reptiles'),
        ('SNAKES', 'Snakes'),
    )

    clan = models.CharField(max_length = 20, choices = CLAN)
    

    def __str__(self):
        return self.clan


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
    clan = models.ForeignKey(Clan , on_delete=models.CASCADE, default = None)
    profileImg = models.ForeignKey(ProfileImg , on_delete=models.CASCADE, blank = True)
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



@receiver(post_save, sender= User)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = Profile(user=instance, clan = Clan.objects.get(clan = 'DOGS'))
        profile.save()
    