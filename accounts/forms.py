# coding=utf-8

from django import forms

from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'name', 'email']


class RegisterForm(forms.ModelForm):

    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def save(self, commit=True):
        super(RegisterForm, self).save(commit=False)
        self.instance.set_password(self.cleaned_data['password'])
        self.instance.save()
        return self.instance

    class Meta:
        model = User
        fields = ['username', 'name', 'email']
