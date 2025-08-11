from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomSignupForm
from .forms import LoginForm

def login_view(request):
    next_url = request.GET.get('next') or request.POST.get('next') or 'home'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username_or_email, password=password)
            if user is not None:
                login(request, user)
                return redirect(next_url)
            else:
                form.add_error(None, 'Username/email or password is incorrect.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'next': next_url})

@login_required
def logout_view(request):    
    logout(request)
    return redirect('pages:home')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomSignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.first_name = form.cleaned_data.get('first_name')
                user.last_name = form.cleaned_data.get('last_name')
                user.email = form.cleaned_data.get('email')
                user.save()
                login(request, user)
                messages.success(request, "Account created successfully! Welcome aboard.")
                return redirect('pages:home')
            else:
                messages.error(request, "There was a problem with your signup. Please try again.")
        else:
            form = CustomSignupForm()

        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('pages:home')

