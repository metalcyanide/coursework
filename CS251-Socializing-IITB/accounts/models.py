from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
##from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user=models.OneToOneField(User)
    City = models.CharField(max_length=200,default='')
    School = models.CharField(max_length=20,default='')
    College = models.CharField(max_length=20,default='')
    About_me = models.CharField(max_length=20,default='')

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)

class Template(models.Model):
    white='white'
    blue='blue'
    yellow='yellow'
    green= 'green'
    CHOICES = (
        (white, 'white'),
        (yellow, 'yellow'),
        (blue, 'blue'),
        (green, 'green'),
    )
    user=models.OneToOneField(User)
    nickname = models.CharField(max_length=200,default='')
    colour = models.CharField(max_length=20,choices=CHOICES,default=white)

def create_template(sender, **kwargs):
    if kwargs['created']:
        user_template = Template.objects.create(user=kwargs['instance'])
post_save.connect(create_template, sender=User)