# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

# class EmailUserCreationForm(UserCreationForm):
#
#     email = forms.EmailField(label="Email", max_length=75)
#
#     print("DDD email {0}".format(email))
#
#     def __init__(self, *args, **kwargs):
#         super(EmailUserCreationForm, self).__init__(*args, **kwargs)
#         del self.fields['username']
#         self.fields.keyOrder = ['email', 'password1', 'password2']
#
#     print("CCC email {0}".format(email))
#
#     def clean_email(self):
#         email = self.cleaned_data['email']
#
#         print("email {0}".format(email))
#
#         try:
#             user = User.objects.get(email=email)
#             if (user):
#                 raise forms.ValidationError("Danny email already exist")
#         except:
#             print("AAA")
#             return email
#
#     def save(self, commit=True):
#         self.instance.username = self.instance.email
#         print("BBB")
#         return super(EmailUserCreationForm, self).save(commit=commit)

class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    # username = forms.CharField(widget=forms.TextInput,label="Username")
    email = forms.EmailField(widget=forms.TextInput,label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Password (again)")

    class Meta:
        model = User
        # fields = ['username', 'email', 'password1', 'password2']
        fields = ['email', 'password1', 'password2']

    def clean(self):
        """
        Verifies that the values entered into the password fields match

        NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
        """
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class EmailAuthenticationForm(AuthenticationForm):
    """
    use email to authenticate
    """
    email = forms.EmailField(label="Email", max_length=75)

    def __init__(self, request=None, *args, **kwargs):
        super(EmailAuthenticationForm, self).__init__(request, *args, **kwargs)
        del self.fields['username']
        self.fields.keyOrder = ['email', 'password']

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Danny authenticate error")

        return self.cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
