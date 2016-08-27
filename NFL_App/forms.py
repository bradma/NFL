from django import forms

class loginForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder' : 'Username', 'style' : 'opacity: 1; background-color: rgb(255, 255, 255); background-position: initial initial; background-repeat: initial initial;'}),
        required=True,
        max_length=10,
    )

    passw = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder' : 'Password', 'style' : 'opacity: 1; background-color: rgb(255, 255, 255); background-position: initial initial; background-repeat: initial initial;'}),
        required=True,
        max_length=15,
    )
