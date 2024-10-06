from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UrlInfo(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)    
    url = models.URLField(max_length=1000, unique=True)
    short_url = models.CharField(max_length=30, unique=True)
    clicks = models.PositiveIntegerField(default=0)  # New field to track clicks

    def __str__(self):
        return f"Short Url for: {self.url} IS: {self.short_url}"
    

class Login(models.Model):
    username = models.CharField(max_length=100)	
    password = models.CharField(max_length=100)

