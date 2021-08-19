from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from OnlineCookbook.accounts.models import Profile

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


"""Custom Login Form used with FBV"""
# class LoginForm(forms.Form):
#     user = None
#
#     email = forms.EmailField()
#
#     password = forms.CharField(
#         widget=forms.PasswordInput(),
#     )
#
#     def clean_password(self):
#         self.user = authenticate(
#             email=self.cleaned_data['email'],
#             password=self.cleaned_data['password'],
#         )
#         if not self.user:
#             raise ValidationError('Email and/or password incorrect')
#
#     def save(self):
#         return self.user
