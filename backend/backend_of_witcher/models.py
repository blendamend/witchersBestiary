from django.db import models
from django.utils import timezone


class Article (models.Model):
    title = models.CharField(max_length=200,
                             default="title")
    text = models.TextField(
        default="there must be a description, but it don't. sorry )':")
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
