from django.contrib import admin
from django.contrib.auth import get_user_model 
from .models import Post,Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(get_user_model())
