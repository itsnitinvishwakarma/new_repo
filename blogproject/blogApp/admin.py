from django.contrib import admin
from blogApp.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','body','author','created','updated','publish','status']
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status','author','created','publish')
    search_fields = ('title','body')
    raw_id_fields = ('author',)
    ordering = ['status','publish']
    date_hierarchy = 'publish'

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','post','created','updated','active']
    list_filter = ('active','updated','created')
    search_fields = ('name','email','body')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
