from  django import forms
from .models import Comments

class CommentAdded(forms.ModelForm) :
    class Meta :
        model =  Comments
        fields = ["text"]
        labels = {"text" : "comment"}