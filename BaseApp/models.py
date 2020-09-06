from django.conf import settings
from django.db import models
from django.utils import timezone


class SiteTime(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    now_date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
