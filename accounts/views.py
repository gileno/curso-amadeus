# coding=utf-8

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import UserForm


@login_required
def edit_user(request):
    form = UserForm(data=request.POST or None, instance=request.user)
    context = {}
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, 'accounts/edit.html', context)
