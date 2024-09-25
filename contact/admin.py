from django.contrib import admin
from .models import ContactRequest

# Register your models here.


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    """
    Admin interface for managing contact requests.
    """
    list_display = ("name", "email", "read")
    list_filter = ("read",)
    search_fields = ("name", "email")
