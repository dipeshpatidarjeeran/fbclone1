from django.contrib import admin
from .models import Post,Like
#
admin.site.register(Like)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_displat=['id','author','photo','title','discription','created_on','liked']	