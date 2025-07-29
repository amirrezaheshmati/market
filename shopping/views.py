from django.shortcuts import render , redirect
from .form import CommentAdded

from .models import Product , Comments
# Create your views here.
def index(request) :
    product = Product.objects.order_by("likes")
    context = {"product" : product}
    return render(request , "shopping/index.html" , context)

def comments(request , product_id) :
    product = Product.objects.get(id = product_id)
    comments = product.comments_set.order_by("date_added")
    context = {"product" : product , "comments" : comments}
    return render(request , "shopping/comments.html" , context)

def add_comment(request , product_id) :
    product = Product.objects.get(id = product_id)
    if request.method != "POST" :
        form = CommentAdded()
    else :
        form = CommentAdded(data=request.POST)
        if form.is_valid() :
            new_comment = form.save(commit=False)
            new_comment.product = product
            new_comment.save()
            return redirect("shopping:comments" , product_id = product_id)
    
    context = {"form" : form , "product" : product}
    return render(request , "shopping/add_comment.html" , context)