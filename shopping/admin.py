from django.contrib import admin
from .models import Product , Comments , Replay , Chat
# Register your models here.
admin.site.register(Product)
admin.site.register(Comments)
admin.site.register(Replay)
admin.site.register(Chat)