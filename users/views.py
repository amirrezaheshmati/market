from django.shortcuts import render , redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .form import Profill
# Create your views here.
def register(request) :
    if request.method != "POST" :
        form = UserCreationForm()
    else :
        form = UserCreationForm(data = request.POST)
        if form.is_valid() :
            new_user = form.save()
            login(request ,new_user)
            return redirect("shopping:index")
        
    context ={"form" : form}
    return render(request ,"registration/register.html" , context)

def fill_profill(request) :
    if request.method != "POST" :
        form = Profill()
    else :
        form = Profill(data=request.POST)
        if form.is_valid() :
            form.save()
            return redirect("shopping:index")
    
    context = {"form" : form}
    return render(request , "registration/profill.html" , context)