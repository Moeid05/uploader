from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

User = get_user_model() 

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            User = get_user_model()
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('uploader : uplaod')
    else:
        form = SignUpForm()
    return render(request, 'users/pages/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('upload')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'users/pages/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('upload')

@login_required
def myFiles(request) :
    user = get_user_model().objects.get(id=request.user.id)
    myfiles = user.myFiles
    context = {'myfiles': myfiles}
    return render(request, 'users/pages/myfiles.html',context=context)