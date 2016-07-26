# coding=utf-8

from django import forms

from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'name', 'email']
