from django.contrib import admin

# Register your models here.
from apps.blog.models import Post

admin.site.register(Post)