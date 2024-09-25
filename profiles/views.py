from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.models import Comment, Post

# Create your views here.


@login_required
def user_profile(request):
    """
    Displays the profile page for the logged-in user.

    Shows their approved and unapproved comments, plus the posts they've liked.

    **Context**

    ``approved_comments``
        User's comments that are approved.
    ``unapproved_comments``
        User's comments waiting for approval.
    ``liked_posts``
        Posts the user has liked.
    ``user``
        The current logged-in user.

    **Template**
    :template:`profiles/user_profile.html`
    """
    user = request.user
    approved_comments = Comment.objects.filter(author=user, active=True)
    unapproved_comments = Comment.objects.filter(author=user, active=False)
    liked_posts = Post.objects.filter(likes=user)

    return render(
        request,
        "profiles/user_profile.html",
        {
            "approved_comments": approved_comments,
            "unapproved_comments": unapproved_comments,
            "liked_posts": liked_posts,
            "user": user,
        },
    )
