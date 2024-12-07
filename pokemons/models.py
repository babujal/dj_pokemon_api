from django.db import models

# Create your models here.
class Pokemon(models.Model):
    poke_type=models.CharField(max_length=200)
    poke_name=models.CharField(max_length=200)