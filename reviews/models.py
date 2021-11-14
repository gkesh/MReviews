from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Publisher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Manga(models.Model):
    title = models.CharField(max_length=250)
    summary = models.TextField()
    author = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    date_serialized = models.DateTimeField(default=timezone.now)
    status = models.BooleanField()
    latest = models.CharField(max_length=250)
    cover = models.ImageField(default='covers/default.jpg', upload_to='covers/')
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title} by {self.author}'


class Rating(models.Model):
    rating = models.FloatField(validators=[MaxValueValidator(10), MinValueValidator(0)])
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.rating} rating on {self.manga.title} by {self.user.username}'


class Review(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.SET_NULL, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review on {self.manga.title} by {self.author.username}'


class UpvoteReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.review.author.username}\'s review upvoted by {self.user.username}'


class DownvoteReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.review.author.username}\'s review downvoted by {self.user.username}'
