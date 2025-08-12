from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model) :
    name = models.CharField(max_length=20)
    price = models.BigIntegerField()
    picture = models.ImageField()
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
    size = models.CharField(choices=SizeChoice.choices , default=SizeChoice.FULL , max_length=100)
    color = models.CharField(choices=ColorChoice.choices , default=ColorChoice.BROWN , max_length=100)
    recieve_code = models.BigIntegerField(default=0)
    count_history = models.PositiveSmallIntegerField(default=0)
    level1 = models.BooleanField(default=False)
    level2 = models.BooleanField(default=False)
    level3 = models.BooleanField(default=False)
    shows = models.SmallIntegerField(default=0)
    date_added = models.CharField(max_length=100)
    date_deleted = models.CharField(max_length=100)
    
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
    
class ChatUser(models.Model) :
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    
class Chat(models.Model) :
    sender = models.ForeignKey(User , on_delete=models.CASCADE , related_name="sender")
    receiver = models.ForeignKey(User , on_delete=models.CASCADE , related_name="receiver")
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    admin_read = models.BooleanField(default=False)
    user_read = models.BooleanField(default=False)

    def __str__(self):
        return self.text