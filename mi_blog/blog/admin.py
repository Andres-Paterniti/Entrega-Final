from django.contrib import admin

# Register your models here.
from .models import Post, Usuario

admin.site.register(Post)
admin.site.register(Usuario)