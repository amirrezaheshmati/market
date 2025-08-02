from  django import forms
from .models import Comments , Replay , Order , Product

class AddToBuyPage(forms.ModelForm) :
    class Meta :
        model = Order
        fields = ["count"]
        labels = {"count" : "count"}

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
        fields = ["name" , "picture" , "price"]
        labels = {"name" : "name" , "picture" : "picture" , "price" : "price"}