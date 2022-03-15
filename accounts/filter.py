import django_filters
from .models import *

class UserSearch(django_filters.FilterSet):

    class Meta:
        model = Person
        fields = ['username', 'location', 'unique_id']