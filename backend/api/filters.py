from django.contrib.auth import get_user_model
from django_filters.rest_framework import FilterSet, filters

from .models import Recipe

User = get_user_model()


class AuthorAndTagFilter(FilterSet):
    tags = filters.AllValuesMultipleFilter(field_name='tags__slug')
    author = filters.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Recipe
        fields = ('tags', 'author')
