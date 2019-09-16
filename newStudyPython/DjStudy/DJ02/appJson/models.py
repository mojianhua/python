from django.db import models

# Create your models here.
class Persions(models.Model):
    name = models.CharField(max_length = 16)
    age = models.IntegerField(default = 0)

    def __str__(self):
        return self.name