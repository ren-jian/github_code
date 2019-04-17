from django.db import models

class Environment(models.Model):
    name = models.CharField(max_length=20)
    nodeip = models.CharField(max_length=20)