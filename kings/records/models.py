from django.db import models

# Create your models here.


class records(models.Model):
    kings = models.CharField(max_length=100, blank=False, unique=True)
    times = models.IntegerField(blank=False, null=False)
