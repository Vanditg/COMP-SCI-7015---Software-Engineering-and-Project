from django import forms

class SignInForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}) )
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))