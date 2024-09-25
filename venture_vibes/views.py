from django.shortcuts import render


def custom_404_view(request, exception):
    """
    Displays a custom 404 error page.
    It is triggered when a requested resource is not found.

    **Template**
    :template:`404.html`
    """
    return render(request, "404.html", status=404)


def custom_500_view(request):
    """
    Displays a custom 500 error page.
    It is triggered when an internal server error occurs.

    **Template**
    :template:`500.html`
    """
    return render(request, "500.html", status=500)
