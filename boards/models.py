from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import Truncator

from django.utils import timezone

import uuid

class Event(models.Model):    

    event_title = models.CharField(max_length=30,default='')
    event_date = models.CharField(max_length=30,default='')
    event_time = models.CharField(max_length=15,default='')
    event_street = models.CharField(max_length=30,default='')
    event_city = models.CharField(max_length=30,default='')
    event_zip = models.CharField(max_length=30,default='')
    event_info = models.CharField(max_length=100,default='')
    event_user = models.ForeignKey(User)
    event_form = models.CharField(max_length=50,default='')
    reader = models.CharField(max_length=50,default='')
    path = models.CharField(max_length=50,default='')  
    pub_date = models.DateTimeField(default=timezone.now)

    EDUCATIONAL = 'EDU'
    ARTSCRAFTS = 'ART'
    SOCIAL = 'SOC'
    LATENIGHT = 'LAT'
    EVENT_CATEGORIES = [ (EDUCATIONAL, 'Educational'), (ARTSCRAFTS, 'Arts & Crafts'), (SOCIAL, 'Social'), (LATENIGHT, 'Late Night'), ]

    category = models.CharField(
        max_length=3,
        choices=EVENT_CATEGORIES,
        default=SOCIAL,
    )

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Create your models here.
class Comment(models.Model):
    comment_text = models.CharField(max_length=200,default='')
    event_id = models.ForeignKey(Event,on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User)
    published_date = models.DateTimeField(default=timezone.now)


