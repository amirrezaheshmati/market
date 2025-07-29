from  django import forms
from .models import Comments , Replay

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