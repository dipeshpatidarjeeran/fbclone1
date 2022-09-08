from django.contrib import admin
from .models import Post
#

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_displat=['id','author','photo','title','discription','created_on']	