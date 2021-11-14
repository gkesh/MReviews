from django.urls import path
from .views import PostListView, PostDetailView
# from . import views
#
#
# urlpatterns = [
#     path('forum/', views.forum, name='forum_home'),
# ]


urlpatterns = [
    path('forum/', PostListView.as_view(), name='forum_home'),
    path('forum/post/<int:pk>/', PostDetailView, name='forum_post'),
]
