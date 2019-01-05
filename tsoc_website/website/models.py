from django.db import models

# Create your models here.

class Participant(models.Model):
    name = models.CharField(max_length = 500, default = 1)
    branch = models.CharField(max_length = 50, default = 1)
    batch = models.IntegerField(max_length = 4, default = 1)
    comments = models.CharField(max_length = 10000, default = 1)

    def __str__(self):
        return self.name