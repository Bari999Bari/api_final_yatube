from django.contrib import admin

from posts.models import Post, Group, Follow, Comment

admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Follow)
admin.site.register(Comment)
