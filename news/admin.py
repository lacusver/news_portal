from django.contrib import admin
from .models import News, Comments, Likes

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'author')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'news','created_at', 'user')

class LikesAdmin(admin.ModelAdmin):
    list_display = ('id', 'news', 'user', 'liked')
admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Likes, LikesAdmin)
