from django.contrib.auth.models import User
from django.db import models

class Fandom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=100,
        unique=True
    )
    group = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='fandom_logos/', null=True, blank=True)

    def __str__(self):
        return f"{self.group} ({self.name})"
    

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    display_name = models.CharField(max_length=50)
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True, blank=True
    )
    bio = models.TextField(
        max_length=300,
        blank=True
    )
    fandom = models.ForeignKey(
        Fandom,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    bias = models.CharField(
        max_length=100,
        blank=True
    )
    location = models.CharField(
        max_length=100,
        blank=True
    )
    joined_on = models.DateTimeField(auto_now_add=True)