from django.urls import path

from . import views

app_name = "shopping"
urlpatterns = [
    path("" , views.index ,name="index"),
    path("comment/<int:product_id>/" , views.comments , name="comments") , 
    path("add_comment/<int:product_id>/" , views.add_comment , name="add_comment"),
    path("add_replay/<int:product_id>/<int:comment_id>" , views.add_replay , name="add_replay"),
    path("buy_page/" , views.buy_page , name="buy_page"),
    path("product_describe/<int:product_id>/" , views.product_describe , name="product_describe"),
    path("buy_list/" , views.buy_list , name="buy_list")
]