from django.shortcuts import render

from .models import Product
# Create your views here.
def index(request) :
    product = Product.objects.order_by("likes")
    context = {"product" : product}
    return render(request , "shopping/index.html" , context)