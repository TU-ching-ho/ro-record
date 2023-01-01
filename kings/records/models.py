from django.db import models

# Create your models here.


class records(models.Model):
    kings = models.CharField(max_length=100)
    times = models.IntegerField(blank=True, null=True)
