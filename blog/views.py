from django.views import generic
from django.shortcuts import render
from .models import Post

# Create your views here.

class PostlistView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED)
    template_name = 'blog/list.html'
    context_object_name = 'posts'