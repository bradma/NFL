from django import forms
from Select.models import user

class change_password(forms.Form):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder' : 'New Password', 'class' : 'form-control', 'id' : 'newPass',}))
    newpassword = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder' : 'Reenter Password', 'class' : 'form-control', 'id' : 'newPassRepeat',}))

class add_team(forms.Form):
    teamName = forms.CharField(max_length=20, label="Team Name")