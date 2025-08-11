from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomSignupForm



def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('pages:home')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('pages:home')

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

