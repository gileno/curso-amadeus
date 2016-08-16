# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage

from rest_framework import generics, permissions

from .serializers import CourseSerializer

from .models import Course, Category


class IndexView(generic.ListView):

    template_name = 'courses/index.html'
    context_object_name = 'courses'
    paginate_by = 1

    def get_queryset(self):
        queryset = Course.objects.filter(is_approved=True)
        q = self.request.GET.get('q', None)
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset


def course(request, slug):
    context = {}
    course = get_object_or_404(Course, slug=slug)
    context['course'] = course
    return render(request, 'courses/course.html', context)


def category(request, slug):
    context = {}
    category = get_object_or_404(Category, slug=slug)
    context['category'] = category
    courses = category.courses.filter(is_approved=True)
    paginator = Paginator(courses, 1)
    try:
        page_number = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    try:
        page_obj = paginator.page(page_number)
    except EmptyPage:
        raise Http404
    context['paginator'] = paginator
    context['page_obj'] = page_obj
    context['courses'] = page_obj.object_list
    return render(request, 'courses/category.html', context)


class CourseListApiView(generics.ListCreateAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Course.objects.filter(is_approved=True)
