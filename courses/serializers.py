from rest_framework import serializers

from .models import Category, Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'name', 'slug', 'description', 'start_date', 'category')
