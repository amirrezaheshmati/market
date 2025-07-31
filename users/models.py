from django.db import models

# Create your models here.
class Acount(models.Model) :
    name = models.CharField(max_length=30)
    number_phone1 = models.BigIntegerField()
    number_phone2 = models.BigIntegerField()
    post_code = models.BigIntegerField()
    addres = models.TextField()
    
    def __str__(self):
        return self.name