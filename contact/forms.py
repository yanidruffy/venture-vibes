from django import forms
from .models import ContactRequest


class ContactForm(forms.ModelForm):
    """
    A form for submitting contact requests.
    """
    class Meta:
        model = ContactRequest
        fields = ("name", "email", "message")
