from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        style = 'font-size: x-large;' \
                'margin-bottom: 30px;' \
                'border: none;' \
                'width: 100%;'
        model = User
        fields = ['username', 'email', 'password']
        widgets = {'username': forms.TextInput(attrs={'placeholder': 'username',
                                                'style': style}),
                   'email': forms.EmailInput(attrs={'placeholder': 'email',
                                                   'style': style}),
                   'password': forms.TextInput(attrs={'placeholder': 'password',
                                                      'style': style})}


class SUForm(forms.Form):
    style = 'font-size: x-large;' \
            'margin-bottom: 30px;' \
            'border: none;' \
            'width: 100%;'
    username = forms.CharField(max_length=22,
                               label="",
                               widget=forms.TextInput(attrs={'placeholder': 'username',
                                                             'style': style}),
                               required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'email',
                                                            'style': style}),
                             required=True,
                             label="")
    password = forms.CharField(max_length=42,
                                label="",
                                widget=forms.TextInput(attrs={'placeholder': 'password',
                                                              'style': style}),
                                required=True)
    password2 = forms.CharField(max_length=42,
                                label="",
                                widget=forms.TextInput(attrs={'placeholder': 're-enter password',
                                                              'style': style}),
                                required=True)

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