from django.contrib import admin
from .models import Manga, Publisher, Rating, Review, UpvoteReview, DownvoteReview


admin.site.register(Manga)
admin.site.register(Publisher)
admin.site.register(Rating)
admin.site.register(Review)
admin.site.register(UpvoteReview)
admin.site.register(DownvoteReview)
