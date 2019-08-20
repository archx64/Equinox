from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']





# class FaceLoginForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput)
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     def clean(self, *args, **kwargs):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#
#         if username and password:
#             user = authenticate(username=username, password=password)
#             if not user:
#                 raise forms.ValidationError('User does not exist')
#             if not user.check_password(password):
#                 raise forms.ValidationError('incorrect password')
#             if not user.is_active:
#                 raise forms.ValidationError('This user is not active')
#
#         return super(FaceLoginForm, self).clean()
