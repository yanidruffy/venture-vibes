from django.views import View
from django.shortcuts import render
from .models import About

# Create your views here.
class AboutView(View):
    def get(self, request):
        about = About.objects.order_by('-updated_on').first()
        return render(
            request,
            "about/about.html",
            {
                'about': about,
            }
        )