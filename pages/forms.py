from django import forms
from pages.models import contact,Newsletter


class NameForm(forms.Form):
    name = forms.CharField(label='Your  name:', max_length=100)
    email = forms.EmailField(label='Your email:')
    subject = forms.CharField(label='Subject', max_length=255)
    message = forms.CharField(widget=forms.Textarea, label='Your message:', max_length=600)

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['name', 'email', 'subject', 'message']

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'