from django.shortcuts import render
from .forms import SignInForm, SignUpForm
from .models import Game


def index(request):
    signin_form = SignInForm()
    games = Game.objects
    return render(request, 'index.html', {'signin_form': signin_form,
                                          'games': games})

def signup(request):
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        signin_form = SignInForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return render(request, 'signup.html', {'signup_form': signup_form,
                                                   'signin_form': signin_form})
    else:
        signup_form = SignUpForm()
        signin_form = SignInForm()
        return render(request, 'signup.html', {'signup_form': signup_form,
                                               'signin_form': signin_form})


def hire(request):
    return render(request, 'hire.html')


def messages(request):
    return render(request, 'messages.html')


def play(request):
    return render(request, 'play.html')


def profile(request):
    return render(request, 'profile.html')
