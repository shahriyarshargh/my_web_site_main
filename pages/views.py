from django.shortcuts import render
from pages.models import contact
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from pages.forms import NameForm, ContactForm,NewsletterForm
from django.contrib import messages

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save(commit=False)
            contact_instance.name = "annonymus"  # Always set name to "ناشناس"
            contact_instance.save()
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data.get('subject', '')  # subject is optional
            message = form.cleaned_data['message']

            contact_entry = contact(name="annonymus", email=email, subject=subject, message=message)
            contact_entry.save()
            return HttpResponse({'success': 'Form submitted successfully!'})
        else:
            return HttpResponse({'status': 'Form is not valid'})
    form = ContactForm()
    return render(request, 'test.html', {'form': form})
