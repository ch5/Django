from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','timestamp','updated']
    list_display_links = ['timestamp']


admin.site.register(Post, PostAdmin)

