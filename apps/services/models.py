from django.db import models
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
