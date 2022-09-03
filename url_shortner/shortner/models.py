from django.db import models


# Create your models here.

class UrlLink(models.Model):
    """link=full url link,short_link= number or alternative something easy to remember"""
    objects = None
    link = models.CharField(max_length=400, null=False)
    short_link = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.short_link}->short link for this {self.link}"
