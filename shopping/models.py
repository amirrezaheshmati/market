from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model) :
    name = models.CharField(max_length=20)
    price = models.BigIntegerField()
    picture = models.ImageField()
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Order(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name="user")
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    count = models.PositiveSmallIntegerField(default=0)
    recieve_code = models.BigIntegerField(default=0)
    count_history = models.PositiveSmallIntegerField(default=0)
    level1 = models.BooleanField(default=False)
    level2 = models.BooleanField(default=False)
    level3 = models.BooleanField(default=False)

class Comments(models.Model) :
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.text[:50]}..."

class Replay(models.Model) :
    comment = models.ForeignKey(Comments , on_delete=models.CASCADE , related_name="replay")
    text = models.TextField()
    likes = models.IntegerField(default=0 )
    date_added = models.DateTimeField(auto_now_add=True )
    
    def __str__(self):
        return f"{self.text[:50]}..."
