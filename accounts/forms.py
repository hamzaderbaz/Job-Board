from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = Profile
#         fields = ['username', 'password']

#     # def clean(self):
#     #     username = self.cleaned_data.get('username')
#     #     password = self.cleaned_data.get('password')

#     #     if username and password:
#     #         user = authenticate(username=username, password=password)
#     #         if user is None:
#     #             raise forms.ValidationError("Please enter a correct username and password.")
#     #         elif not user.is_active:
#     #             raise forms.ValidationError("This account is inactive.")
#     #     return self.cleaned_data
    


class UserForm(forms.ModelForm):
    class Meta:
       model = User
       fields = ['username', 'first_name', 'last_name', 'email']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'phone_number', 'image']





# class LoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
#         self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
