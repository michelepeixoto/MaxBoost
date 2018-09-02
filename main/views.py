from django.shortcuts import render, redirect
from .forms import SignInForm, SignUpForm, PlayForm
from .models import Game, User, GameStat


# starting load procedure for all pages
def load_start():
    signin_form = SignInForm()
    users_online = get_users_online()
    return signin_form


def get_users_online():
    online_users = User.objects.filter(is_online=True)
    print(online_users)
    users_list = []
    for user in online_users:
        users_list.append(user.username)
    return users_list


def get_friends_list(user_name):
    friends_list = User.objects.get(username=user_name).friends.split(',')
    return friends_list


def index(request):
    users_online = get_users_online()
    friends_list = get_friends_list('test')
    signin_form = SignInForm()
    games = Game.objects
    return render(request, 'index.html', {'signin_form': signin_form,
                                          'users_online': users_online,
                                          'friends_list': friends_list,
                                          'games': games})

def signup(request):
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        signin_form = SignInForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('/profile/{}'.format(signup_form.cleaned_data['username']))
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


def profile(request, user_name):
    user = User.objects.get(username=user_name) # change this to username from request
    user_stats = GameStat.objects.filter(username=user_name)
    game_count = 0
    highest_game_count = 0
    most_played = ""
    for stat in user_stats:
        game_count = stat.times_played
        if game_count >= highest_game_count:
            highest_game_count = game_count
            most_played = stat.game_title
    try:
        most_played = Game.objects.get(title=most_played).picture
    except:
        most_played = None
    signin_form = SignInForm()
    return render(request, 'profile.html', {'user': user,
                                            'user_stats': user_stats,
                                            'most_played': most_played,
                                            'signin_form': signin_form})
