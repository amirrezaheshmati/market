from django.db import models

# Create your models here.
class Product(models.Model) :
    name = models.CharField(max_length=20)
    price = models.BigIntegerField()
    picture = models.ImageField()
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name