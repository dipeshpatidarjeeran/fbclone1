from django.contrib import admin
from .models import Post
#

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_displat=['id','post_user','photo','title','discription',]	