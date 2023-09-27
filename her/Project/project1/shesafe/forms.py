from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    login_username = forms.CharField(max_length=100)
    login_password = forms.CharField(widget=forms.PasswordInput)

