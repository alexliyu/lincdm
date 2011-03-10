from django.db import models
from datetime import datetime
# Create your models here.
class siteSetting(models.Model):
        sitename = models.CharField(max_length=15)
        sitetitle = models.CharField(default='', max_length=50)
    
