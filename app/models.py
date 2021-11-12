from django.db import models

# Create your models here.
class Service(models.Model):

     
    service_icon = models.CharField(max_length=120)
    service_title = models.CharField(max_length=120)
    service_des = models.TextField(max_length=120)


class Width(models.Model):
    width_data = models.CharField(max_length=120) 