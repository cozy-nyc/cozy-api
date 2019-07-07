from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Service(models.Model):
    """
        This is a model for the multiple different services and will allow us to see if
        they are online or not. The services include all the different apps, forum,store,
        and stream

        Attributes:
            service: Name of the service Ex: Forums
            status: Returns the status of a service, whether it be offline or online
            message: An object with an important boolean, as well as a message detailing
                     the status of the service
    """
    ONLINE = 'online'
    OFFLINE = 'offline'
    STATUSES = [
        (ONLINE, 'online'),
        (OFFLINE, 'offline')
    ]

    service = models.TextField(max_length = 50, unique = True, blank=False)
    status = models.CharField(max_length = 10, choices = STATUSES, default = ONLINE)
    message = models.OneToOneField(ServiceMessage, on_delete=models.CASCADE)

class ServiceMessage(models.Model):
    """
        This is a model that stores information on messages regarding the status of the
        different services within the API

        Attributes:
            important: boolean that displays whether the message is important or not
            text: string displaying the message associated with the service's status
    """
    important = models.BooleanField(default = False)
    text = models.TextField(max_length = 200, blank = False)

@receiver(post_save, sender = Service)
def create_serviceMessage_for_new_service(sender, created, instance **kwargs):
    if created:
        serviceMessage = ServiceMessage(important = False, text = "Service is Online")
        serviceMessage.save()
        instance.message = serviceMessage
        instance.save()


class Profile(models.Model):
    """
        This is a model for user's profile.

        Attributes:
            user: The user related to the profile.
            profileImg: The user's profile image.
            location: Optional location text field.
            bio: Text field for user's biography
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length = 250, blank = True)
    profileImg = models.ImageField(upload_to='images/')
    location = models.TextField(max_length=50, blank=True)

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
