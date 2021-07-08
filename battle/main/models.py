from django.db import models

# Create your models here.
class Submission(models.Model):
    name = models.CharField(max_length=100)
    total = models.IntegerField()
    r1 = models.IntegerField()
    r2 = models.IntegerField()
    r3 = models.IntegerField()
    r4 = models.IntegerField()
    r5 = models.IntegerField()
