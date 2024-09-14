from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import CommentForm
from .models import Post, Comment

# Create your views here.

class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED)
    template_name = 'blog/list.html'
    context_object_name = 'posts'

class PostDetailView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(active=True).order_by('-created')
        comment_count = post.comments.filter(active=True).count()
        comment_form = CommentForm()
        return render(
            request,
            'blog/post_detail.html',
            {
                'post': post,
                'comments': comments,
                'comment_count': comment_count,
                'comment_form': comment_form,
            }
        )

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(data=request.POST)
        comments = post.comments.filter(active=True).order_by('-created')
        comment_count = post.comments.filter(active=True).count()

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

            comment_form = CommentForm()

        else:
            messages.add_message(
                request, messages.ERROR,
                'Comment has not been submitted due to an Error'
            )
        
        return render(
            request,
            'blog/post_detail.html',
            {
                'post': post,
                'comments': comments,
                'comment_count': comment_count,
                'comment_form': comment_form(),
            }
        )

def comment_edit(request, slug, comment_id):
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.active = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment updated and awaiting approval!')
            return HttpResponseRedirect(reverse('blog:post_detail', args=[slug]))
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')
    
    return render(
        request,
        'blog/post_detail.html',
        {
            'post': post,
            'comments': post.comments.filter(active=True).order_by('-created'),
            'comment': comment,
            'comment_form': comment_form,
            'comment_count': post.comments.filter(active=True).count(),
            'editing_comment': True,
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