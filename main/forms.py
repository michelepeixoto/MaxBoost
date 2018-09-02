from django import forms
from .models import User, Game


def get_all_games():
    game_choices = [('','select a game'),]
    all_games = Game.objects.all()
    for i in range(len(all_games)):
        game_choices.append((i, all_games[i].title))
    return game_choices


GAMES_LIST = get_all_games()


class SignUpForm(forms.ModelForm):
    class Meta:
        style = 'font-size: x-large;' \
                'margin-bottom: 30px;' \
                'border: none;' \
                'width: 100%;'
        model = User
        fields = ['username', 'email', 'password', 'password2', 'is_booster', 'hire_price']
        widgets = {'username': forms.TextInput(attrs={'placeholder': 'username',
                                                      'id': 'username',
                                                      'style': style}),
                   'email': forms.EmailInput(attrs={'placeholder': 'email',
                                                    'id': 'email',
                                                    'style': style}),
                   'password': forms.PasswordInput(attrs={'placeholder': 'password',
                                                          'id': 'password1',
                                                          'style': style}),
                   'password2': forms.PasswordInput(attrs={'placeholder': 'repeat password',
                                                           'id': 'password2',
                                                          'style': style}),
                   'is_booster': forms.CheckboxInput(attrs={'id': 'is_booster',
                                                            'style': 'font-size: 400%; '
                                                                     'margin-bottom: 30px;'}),
                   'hire_price': forms.NumberInput(attrs={'id': 'hire_price',
                                                          'style': style + 'display: none;'})}

    def clean(self):
        cleaned_data = super().clean()
        pw1 = cleaned_data.get('password')
        pw2 = cleaned_data.get('password2')
        if pw1 != pw2:
            self.add_error('password2', "Passwords don't match")


class SignInForm(forms.Form):
    style = ""
    username = forms.CharField(max_length=22,
                               label="",
                               widget=forms.TextInput(attrs={'placeholder': 'username',
                                                             'style': style}),
                               required=True)
    password = forms.CharField(max_length=42,
                                label="",
                                widget=forms.TextInput(attrs={'placeholder': 'password',
                                                              'style': style}),
                                required=True)


class PlayForm(forms.Form):
    game_title = forms.ChoiceField(choices=GAMES_LIST,
                                   widget=forms.Select())
