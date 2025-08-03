from  django import forms
from .models import Comments , Replay , Order , Product

class AddToBuyPage(forms.ModelForm) :
    class Meta :
        model = Order
        fields = ["count" , "size" , "color"]
        labels = {"count" : "count" , "size" : "size" , "color" : "color"}

class CommentAdded(forms.ModelForm) :
    class Meta :
        model =  Comments
        fields = ["text"]
        labels = {"text" : "comment"}

class ReplayAdded(forms.ModelForm) : 
    class Meta :
        model = Replay
        fields = ["text"]
        labels = {"text" : "Replay"}
        
class AddProduct(forms.ModelForm) :
    class Meta :
        model = Product
        fields = ["name" , "picture_red" , "picture_green" , "picture_blue" , "picture_brown" ,
                  "picture_black" , "picture_white" , "picture_silver" , "price"]
        labels = {"name" : "name" , "picture_red" : "picture red" ,"picture_green" : "picture green",
                  "picture_blue" : "picture blue" ,"picture_brown" : "picture brown" ,"picture_silver" : "picture silver" , 
                  "picture_black" : "picture black" , "picture_white" :"picture white", "price" : "price"}