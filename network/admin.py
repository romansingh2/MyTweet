from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import Post, User, PostLike
"""
class User(admin.ModelAdmin):
    search_fields = ['user__username']
    class Meta:
        model = User
"""
class PostLikeAdmin(admin.TabularInline):
    model = PostLike

class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['tweet', 'user__username', 'user_email']
    class Meta: 
        model = Post
    
admin.site.register(Post, PostAdmin)
admin.site.register(User)

