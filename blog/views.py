from django.views import generic
from django.shortcuts import render
from .models import Post

# Create your views here.

class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED)
    template_name = 'blog/list.html'
    context_object_name = 'posts'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

def index(request):
    latest_post = Post.objects.filter(status=Post.Status.PUBLISHED).order_by('-publish').first()
    return render(
        request,
        'blog/index.html',
        {
            'latest_post': latest_post
        },
    )