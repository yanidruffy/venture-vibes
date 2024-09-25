from django.views import View
from django.shortcuts import render
from .models import About


# Create your views here.
class AboutView(View):
    """
    Renders the most recent information on the About page.

    Displays an individual instance of :model:`about.About`.

    **Context**
    ``about``
        The most recent instance of :model:`about.About`.

    **Template**
    :template:`about/about.html`
    """
    def get(self, request):
        about = About.objects.order_by("-updated").first()
        return render(
            request,
            "about/about.html",
            {
                "about": about,
            },
        )
