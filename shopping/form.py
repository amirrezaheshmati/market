from  django import forms
from .models import Comments , Replay , Product

class AddToBuyPage(forms.ModelForm) :
    class Meta :
        model = Product
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