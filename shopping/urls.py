from django.urls import path

from . import views

app_name = "shopping"
urlpatterns = [
    path("" , views.index ,name="index"),
    path("comment/<int:product_id>/" , views.comments , name="comments") , 
    path("add_comment/<int:product_id>/" , views.add_comment , name="add_comment"),
]