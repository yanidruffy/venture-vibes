from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    A form for submitting comments.
    """
    class Meta:
        model = Comment
        fields = ("body",)
