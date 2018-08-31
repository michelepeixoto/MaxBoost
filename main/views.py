from django.shortcuts import render
from .forms import SignInForm, SignUpForm, PlayForm
from .models import Game, User, GameStat


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
    if request.method == 'POST':
        form = PlayForm(request.POST)
        if form.is_valid():
            # return list of users playing form.cleaned_data['game_title']
            return render(request, 'play.html', {'play_form' : form})
        else:
            return render(request, 'play.html', {'play_form' : form})
    else:
        form = PlayForm()
    return render(request, 'play.html', {'play_form' : form})


def profile(request):
    user = User.objects.get(username='test') # change this to username from request
    user_stats = GameStat.objects.filter(username='test')
    game_count = 0
    highest_game_count = 0
    most_played = ""
    for stat in user_stats:
        game_count = stat.times_played
        if game_count > highest_game_count:
            highest_game_count = game_count
            most_played = stat.game_title
    most_played = Game.objects.get(title=most_played).picture
    signin_form = SignInForm()
    return render(request, 'profile.html', {'user': user,
                                            'user_stats': user_stats,
                                            'most_played': most_played,
                                            'signin_form': signin_form})
