from django.db import models

# Create your models here.
class ListingSite(models.Model):
    sitename = models.CharField(max_length=250,unique=True)
    url = models.URLField(null=True,blank=True,unique=True)
    invites = models.PositiveBigIntegerField(default=0)
    
    def __str__(self):
        return self.sitename
