from django.shortcuts import render

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