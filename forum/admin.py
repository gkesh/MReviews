from django.contrib import admin
from .models import Post, Comment, Favourite, PostUpvote, CommentUpvote, PostDownvote, CommentDownvote

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Favourite)
admin.site.register(PostUpvote)
admin.site.register(PostDownvote)
admin.site.register(CommentUpvote)
admin.site.register(CommentDownvote)
