from django.shortcuts import render , redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .form import Profill
from .models import Acount
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

def fill_profill(request , totall_price) :
    try :
        acount = Acount.objects.get(user = request.user)
    except Acount.DoesNotExist :
        acount = Acount(user = request.user)
    if request.method != "POST" :
        form = Profill(instance=acount)
    else :
        form = Profill(instance=acount , data=request.POST)
        if form.is_valid() :
            form.save()
            return redirect(f"https://zarinp.al/python_developer?amount={totall_price}")
    
    context = {"form" : form , "totall_price" : totall_price}
    return render(request , "registration/profill.html" , context)