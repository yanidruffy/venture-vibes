from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request,messages.SUCCESS,
                """Your message has been received! We will respond to your message within 3 business days. 
                Stay tuned for our reply."""
            )
            return HttpResponseRedirect(reverse('blog:index'))
    else:
        contact_form = ContactForm()

    return render(
        request,
        'contact/contact.html',
        {'contact_form': contact_form}
        )