import django_filters
from django_filters import filters
from .models import *
from django.db.models import Q
from products.models import Products,Category

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Products
        fields = ('category',)
    def __init__(self, *args, **kwargs):
        super(CategoryFilter, self).__init__(*args, **kwargs)
        self.filters['category'].extra.update(
            {'empty_label': 'category'})
            
class SectionFilter(django_filters.FilterSet):
    class Meta:
        model = Products
        fields = ('section',)
    def __init__(self, *args, **kwargs):
        super(SectionFilter, self).__init__(*args, **kwargs)
        self.filters['section'].extra.update(
            {'empty_label': 'section'})



