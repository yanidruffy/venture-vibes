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
    template_name = "blog/list.html"
    context_object_name = "posts"
    paginate_by = 3


class PostDetailView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.all().order_by("-created")
        comment_count = post.comments.filter(active=True).count()
        comment_form = CommentForm()
        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_count": comment_count,
                "comment_form": comment_form,
                "user": request.user,
            },
        )

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(data=request.POST)
        comments = post.comments.all().order_by("-created")
        comment_count = post.comments.filter(active=True).count()

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Comment submitted and awaiting approval"
            )

            comment_form = CommentForm()

        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Comment has not been submitted due to an Error",
            )

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_count": comment_count,
                "comment_form": comment_form,
                "user": request.user,
            },
        )


def comment_edit(request, slug, comment_id):

    if request.method == "POST":
        post = get_object_or_404(Post, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.active = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Comment updated and awaiting approval!"
            )
            return HttpResponseRedirect(
                reverse("blog:post_detail", args=[slug])
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                "Error updating comment!"
            )

    return HttpResponseRedirect(
        reverse("blog:post_detail", args=[slug])
    )


def comment_delete(request, slug, comment_id):
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS,
            "Comment deleted successfully!"
        )
    else:
        messages.add_message(
            request, messages.ERROR,
            "You are not allowed to delete this comment."
        )

    return HttpResponseRedirect(
        reverse("blog:post_detail", args=[slug])
    )


def index(request):
    latest_post = (
        Post.objects.filter(status=Post.Status.PUBLISHED)
            .order_by("-publish").first()
    )
    return render(
        request,
        "blog/index.html",
        {"latest_post": latest_post},
    )


def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(
        reverse("blog:post_detail", args=[slug])
    )
