from django.db import models

# Create your models here.
class myupadtes(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pictures')
    desc = models.TextField()