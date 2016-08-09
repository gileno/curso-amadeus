# coding=utf-8

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView
from django.http import HttpResponseForbidden

from rolepermissions.shortcuts import assign_role
from rolepermissions.verifications import has_role
from rolepermissions.mixins import HasRoleMixin

from .models import User
from .forms import UserForm, RegisterForm


@login_required
def edit_user(request):
    form = UserForm(data=request.POST or None, instance=request.user)
    context = {}
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, 'accounts/edit.html', context)


class RegisterView(CreateView):

    model = User
    form_class = RegisterForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        form.save()
        assign_role(form.instance, 'student')
        context = self.get_context_data(form=form)
        context['success'] = True
        return self.render_to_response(context)


class CoursesView(HasRoleMixin, TemplateView):

    allowed_roles = ['student']
    template_name = 'accounts/courses.html'
