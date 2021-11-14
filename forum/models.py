from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=500, null=False)
    content = models.TextField(null=False)
    image = models.ImageField(default='covers/default.jpg', upload_to='posts/')
    highlight = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} by {self.author.username}'


class Comment(models.Model):
    content = models.TextField(null=False)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.commenter.username}'


class PostReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class CommentReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Favourite(PostReaction):
    def __str__(self):
        return f'{self.post.title} hearted by {self.user.username}'


class PostUpvote(PostReaction):
    def __str__(self):
        return f'{self.post.title} upvoted by {self.user.username}'


class PostDownvote(PostReaction):
    def __str__(self):
        return f'{self.post.title} downvoted by {self.user.username}'


class CommentUpvote(CommentReaction):
    def __str__(self):
        return f'{self.comment.post.title}\'s comment upvoted by {self.user.username}'


class CommentDownvote(CommentReaction):
    def __str__(self):
        return f'{self.comment.post.title}\'s comment downvoted by {self.user.username}'
