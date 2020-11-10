from django.db import models

# Create your models here.
class Info(models.Model):
    short_info = models.CharField(max_length=250)
class Du_lead(models.Model):
    du_lead = models.CharField(max_length=250)
class Manager(models.Model):
    manager = models.CharField(max_length=250)
class Ams(models.Model):
    ams = models.CharField(max_length=250)
class Leads(models.Model):
    leads = models.CharField(max_length=250)
