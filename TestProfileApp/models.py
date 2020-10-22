from django.db import models

# Create your models here.
class UserProfile(models.Model):
    Id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100, null=True,blank=True)
    LastName = models.CharField(max_length=100, null=True,blank=True)
    
