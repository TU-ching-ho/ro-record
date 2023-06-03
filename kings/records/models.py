from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class records(models.Model):
    kings = models.CharField(max_length=100, blank=False, unique=False)
    times = models.IntegerField(blank=False, null=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
