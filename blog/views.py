from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post

# Create your views here.

class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED)
    template_name = 'blog/list.html'
    context_object_name = 'posts'

class PostDetailView(View):
    def get(self,request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.all().order_by('-created')
        comment_count = post.comments.filter(active=True).count()
        return render(
            request,
            'blog/post_detail.html',
            {
                'post': post,
                'comments': comments,
                'comment_count': comment_count,
            }
        )

def index(request):
    latest_post = Post.objects.filter(status=Post.Status.PUBLISHED).order_by('-publish').first()
    return render(
        request,
        'blog/index.html',
        {
            'latest_post': latest_post
        },
    )