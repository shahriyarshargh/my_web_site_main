from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.user.is_authenticated:
        msg = f'You are already logged in as {request.user.username}'
        return render(request, 'login.html', {'msg': msg})

    msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            msg = 'Invalid username or password'

    return render(request, 'login.html', {'msg': msg})

        

def logout_view(request):
    return render(request, 'logout.html')
def signup_view(request):
    if request.method == 'POST':
        # Handle signup logic
        pass
    return render(request, 'signup.html')