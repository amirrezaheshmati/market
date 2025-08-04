from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model) :
    name = models.CharField(max_length=20)
    price = models.BigIntegerField()
    picture_red = models.ImageField()
    picture_green = models.ImageField()
    picture_blue = models.ImageField()
    picture_black = models.ImageField()
    picture_white = models.ImageField()
    picture_brown = models.ImageField()
    picture_silver = models.ImageField()
    likes = models.ManyToManyField(User , blank=True , related_name="like")
    
    def __str__(self):
        return self.name
    
class SizeChoice(models.TextChoices) :
    FULL = "100%" , "100%"
    HALF = "50%" , "50%"
    QUARTER = "25%" , "25%"
    
class ColorChoice(models.TextChoices) :
    RED = "red" , "red"
    GREEN = "green" , "green"
    BLUE = "blue" , "blue"
    BLACK = "black" , "black"
    WHITE = "white" , "white"
    BROWN = "brown" , "brown"
    SILVER = "silver" , "silver"
    
class Order(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="prod")
    date_added = models.DateTimeField(auto_now_add=True)
    count = models.PositiveSmallIntegerField(default=0)
    size = models.CharField(choices=SizeChoice.choices , default=SizeChoice.FULL)
    color = models.CharField(choices=ColorChoice.choices , default=ColorChoice.BROWN)
    recieve_code = models.BigIntegerField(default=0)
    count_history = models.PositiveSmallIntegerField(default=0)
    level1 = models.BooleanField(default=False)
    level2 = models.BooleanField(default=False)
    level3 = models.BooleanField(default=False)
    shows = models.SmallIntegerField(default=0)
    date_added = models.CharField()
    date_deleted = models.CharField()
    
class Comments(models.Model) :
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.ManyToManyField(User , blank=True , related_name="like_commnet")
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.text[:50]}..."

class Replay(models.Model) :
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments , on_delete=models.CASCADE , related_name="replay")
    text = models.TextField()
    likes = models.IntegerField(default=0 )
    date_added = models.DateTimeField(auto_now_add=True )
    
    def __str__(self):
        return f"{self.text[:50]}..."
