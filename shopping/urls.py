from django.urls import path

from . import views

app_name = "shopping"
urlpatterns = [
    path("" , views.index ,name="index"),
    path("comment/<int:product_id>" , views.comments , name="comments") , 
]