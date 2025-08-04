from django.shortcuts import render
from pages.models import contact
from django.http import HttpResponse,JsonResponse
from pages.forms import NameForm, ContactForm

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    if request.method == 'POST'
        form = ContactForm(request.POST)
        if form.is__valid():
            form.save()
    form = ContactForm()
    return render(request, 'contact.html',{'form' : form})

def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            contact_entry = contact(name=name, email=email, subject=subject, message=message)
            contact_entry.save()
            return HttpResponse({'success': 'Form submitted successfully!'})
        else:
            return HttpResponse({'status': 'Form is not valid'})
    form = ContactForm()
    return render(request, 'test.html',{'form':form})
