from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        msg = f'user is already logged in as {request.user.username}'
    else:
        msg = 'please log in'
        return render(request, 'login.html', {'msg': msg})
    
def logout_view(request):
    return render(request, 'logout.html')
def signup_view(request):
    if request.method == 'POST':
        # Handle signup logic
        pass
    return render(request, 'signup.html')