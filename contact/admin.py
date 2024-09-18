from django.contrib import admin
from .models import ContactRequest

# Register your models here.

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'read')
    list_filter = ('read',)
    search_fields = ('name', 'email')