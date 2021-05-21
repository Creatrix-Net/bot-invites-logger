from django.db import models

# Create your models here.
class ListingSite(models.Model):
    sitename = models.CharField(max_length=250)
    url = models.URLField(null=True,blank=True)
    invites = models.PositiveBigIntegerField(default=0)
