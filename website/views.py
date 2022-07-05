from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from website.models import Contact
from .forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            new_name = form.save(commit=False)
            new_name.name = 'Unknown'
    
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your ticket submited successfully")
        else:
            messages.add_message(request, messages.ERROR,"Your ticket didnt submited")
    form = ContactForm()
    
    return render(request, 'website/contact.html', {'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def maintenance_view(request):
    return render(request, 'website/maintenance.html')