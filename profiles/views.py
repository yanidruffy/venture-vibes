from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.models import Comment, Post

# Create your views here.

@login_required
def user_profile(request):
    user = request.user
    approved_comments = Comment.objects.filter(author=user, active=True)
    unapproved_comments = Comment.objects.filter(author=user, active=False)
    liked_posts = Post.objects.filter(likes=user)

    return render(
        request,
        'profiles/user_profile.html',
        {
            'approved_comments': approved_comments,
            'unapproved_comments': unapproved_comments,
            'liked_posts': liked_posts,
            'user': user,
        }
    )

