# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class ForumUser(models.Model):
    user = models.OneToOneField(User)
    photo = models.ImageField(upload_to='profile_photo',blank=True)
    def __unicode__(self):
        return self.user.username

class Article(models.Model):
    head = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    user = models.ForeignKey('ForumUser',models.SET_NULL,null=True)

    def __unicode__(self):
        return self.head



# Create your models here.
