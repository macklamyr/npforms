from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter
from .models import Post, Author


class PostFilter(FilterSet):
    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Автор',
        empty_label='Все',
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': [],
            'date_in': [
                'lt',
            ],
        }
