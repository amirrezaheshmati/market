from django.shortcuts import render , redirect
from django.db.models import Q
from .form import CommentAdded , ReplayAdded , AddToBuyPage
from .models import Product , Comments , Order
from random import choice
# Create your views here.
def index(request) :
    return render(request , "shopping/index.html")

def product_list(request) :
    product = Product.objects.order_by("likes")
    context = {"product" : product}
    return render(request , "shopping/product_list.html" , context)
    
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

def add_replay(request , comment_id , product_id) :
    product = Product.objects.get(id = product_id)
    comment = Comments.objects.get(id = comment_id)
    if request.method != "POST" :
        form = ReplayAdded()
    else :
        form = ReplayAdded(data=request.POST)
        if form.is_valid() :
            new_replay = form.save(commit=False)
            new_replay.comment = comment
            new_replay.save()
            return redirect("shopping:comments" ,product_id = product_id )
    
    context = {"form" : form , "comment" : comment , "product" : product}
    return render(request , "shopping/add_replay.html" , context)

def product_describe(request , product_id) :
    product = Product.objects.get(id = product_id)
    try :
        order = Order.objects.get(user = request.user,
                                  product = product)
    except Order.DoesNotExist :
        order = Order(user = request.user , 
                      product = product)
    if request.method != "POST" :
        form = AddToBuyPage(instance=order)
    else :
        form = AddToBuyPage(instance=order, data=request.POST)
        if form.is_valid() :
            form.save()
            return redirect("shopping:buy_page")

    context = {"form" : form , "product" : product}
    return render(request , "shopping/product_describe.html" , context)

def buy_page(request) :
    return render(request , "shopping/buy_page.html")

def buy_list(request) :
    order = Order.objects.filter(user = request.user ,count__gt = 0)
    totall_price = 0
    for pro in order :
        pro.level1 = True
        totall_price += pro.count * pro.product.price
        pro.save()
    context = {"order" : order , "totall_price" : totall_price}
    return render(request , "shopping/buy_list.html" , context)

def buy_action(request) :
    numbers = list(n for n in range(10))
    order = Order.objects.filter(user = request.user , level2 = True)
    revieve_code = ""
    for x in range(8) :
        num = choice(numbers)
        revieve_code += str(num)
    for pro in order :
        if pro.recieve_code == 0 :
            pro.recieve_code = revieve_code
            pro.save()
    context = {"order" : order}
    return render(request , "shopping/buy_action.html" , context)

def buy_history(request) :
    order = Order.objects.filter(user = request.user , level3 = True)
    context = {"order" : order}
    return render(request , "shopping/buy_history.html" , context)