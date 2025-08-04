from django.urls import path

from . import views

app_name = "shopping"
urlpatterns = [
    path("" , views.index ,name="index"),
    path("products/" , views.product_list , name="product_list") ,
    path("comment/<int:product_id>/" , views.comments , name="comments") , 
    path("add_comment/<int:product_id>/" , views.add_comment , name="add_comment"),
    path("add_replay/<int:product_id>/<int:comment_id>" , views.add_replay , name="add_replay"),
    path("buy_page/" , views.buy_page , name="buy_page"),
    path("product_describe/<int:product_id>/" , views.product_describe , name="product_describe"),
    path("buy_list/" , views.buy_list , name="buy_list") ,
    path("buy_action/", views.buy_action , name="buy_action"),
    path("delete_user/<int:product_id>/" , views.delete_user , name="delete_user"),
    path("buy_history/" , views.buy_history , name="buy_history"),
    path("buy_history/" , views.buy_history , name="buy_history"),
    path("admin_panel/" , views.admin_panel , name="admin_panel"),
    path("admin_action/" , views.admin_action , name="admin_action"),
    path("admin_action/<int:product_id>/" , views.delete_admin_product , name="delete"),
    path("admin_history/" , views.admin_history , name="admin_history"), 
    path("like_post/<int:post_id>/" , views.like_post , name="like_post"),
    path("like_comment/<int:comment_id>/<int:product_id>/" , views.like_comment , name="like_comment")
]