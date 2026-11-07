import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

WELCOME_MESSAGES = [
    "What's Going On Here?",
    "Yoo Crazy",
    "Fresh energy, new people, and a lot of adventure",
    "The vibe is changing",
]


def enter(request):
    if request.user.is_authenticated:
        return redirect('blog_page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['welcome_message'] = random.choice(WELCOME_MESSAGES)
            return redirect('blog_page')

        return render(request, 'main/enter.html', {'error': 'Invalid username or password.'})

    return render(request, 'main/enter.html')



def signup(request):
    if request.user.is_authenticated:
        return redirect('blog_page')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            request.session['welcome_message'] = random.choice(WELCOME_MESSAGES)
            return redirect('blog_page')

        return render(request, 'main/enter.html', {'signup_error': form.errors})

    return render(request, 'main/enter.html')

def logout_user(request):
    logout(request)
    return redirect('main_enter')