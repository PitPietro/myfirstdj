# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        msg = 'Title: {}, Content: {}, Author: {}, Date Posted: {}' \
            .format(self.title, self.content, self.author, self.date_posted)
        return msg

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
