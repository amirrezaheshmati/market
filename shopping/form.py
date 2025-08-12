from  django import forms
from .models import Comments , Replay , Order , Product , Chat
from PIL import Image

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
        fields = ["name"  , "price" , "picture"]
        labels = {"name" : "name" , "picture" : "picture", "price" : "price"}
        widgets = {"name" : forms.Textarea(attrs={'style': 'width:200px; height: 40px;'}),
                "price" : forms.Textarea(attrs={'style': 'width:150px; height: 40px;'})}
        
    def clean_picture(self):
        photo = self.cleaned_data.get('picture')

        if photo:
            img = Image.open(photo)
            width, height = img.size
            ratio = width / height

            expected_ratio = 5 / 4  # نسبت مورد نظر

            # کمی خطای کوچک مجاز (برای جلوگیری از مشکل اعشار)
            if not (abs(ratio - expected_ratio) < 0.01):
                raise forms.ValidationError("نسبت تصویر باید 5 به 4 باشد.")

        return photo

class Chats(forms.ModelForm) :
    class Meta :
        model = Chat
        fields = ["text"]
        labels = {"text" : ""}
        widgets = {"text" : forms.Textarea(attrs={'style': 'width:100%; height: 40px;'})}