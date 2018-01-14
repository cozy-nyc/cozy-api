from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
import datetime
# Create your models here.

class Board(models.Model):

    name = models.CharField(max_length=50, db_index=True)
    abbreviation = models.CharField(max_length=10, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)
    lastUpdated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'board'
        verbose_name_plural = 'boards'


    def latestPost(self):
        lastPost = self.thread.order_by('created').first()
        if lastPost:
            return lastPost
        return None



class Thread(models.Model):
    title = models.CharField(max_length=250, db_index=True)
    content = models.TextField(default = '')
    slug = models.SlugField(max_length=250, db_index=True)
    created = models.DateTimeField(auto_now = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name='thread', on_delete=models.CASCADE)
    numberOfReplies = models.PositiveIntegerField(default = 0)
    viewCount = models.PositiveIntegerField(default = 0)
    numberOfImages = models.PositiveIntegerField(default = 0)
    image = models.ImageField(max_length=255,
                              upload_to='uploads/forum/post',
                              blank=True,
                              default='',
                              null=True)
    latestReplyTime = models.DateTimeField(auto_now = True)


    def __str__(self):
        self.title

    class Meta:
        ordering = ['created']
        verbose_name = 'thread'
        verbose_name_plural = 'threads'

    def getLatestReply(self):
        latestReply = self.posts.order_by('created').first()
        if latestReply:
            return latestReply
        return latestReply

    def save(self, **kwargs):
        if not self.pk:
            slug = self.title
            slug = slug.lower()
            slug = slug.replace(" ", "-")
            self.slug = slug

        if self.pk:
            self.latestReply = self.getLatestReply()
            self.numberOfReplies = len(self.posts)


        super(Item, self).save(**kwargs)


class Post(models.Model):
    content = models.TextField(default = '')
    created = models.DateTimeField(auto_now = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(max_length = 255,
                              upload_to='uploads/forum/post',
                              blank=True,
                              default='',
                              null=True)


    def __str__(self):
        self.content

    class Meta:
        ordering = ['created']
        verbose_name = 'post'
        verbose_name_plural = 'posts'
