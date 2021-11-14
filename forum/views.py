from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@login_required()
def forum(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'forum/home.html', context)


@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    # Default Convention for templates in class based view
    # <app>/<model>_<viewtype>.html
    model = Post
    template_name = 'forum/home.html'
    context_object_name = 'posts'
    ordering = ['-date_created']


@method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    model = Post
    template_name = 'forum/post.html'
    context_object_name = 'post'
