from django.contrib import admin
from .models import Post,Like,Comment,Student
#
admin.site.register(Like)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_displat=['id','author','photo','title','discription','created_on','liked']	

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_displat=['user','post','content','created_on']

@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
	list_displat=['id','name','roll','city']