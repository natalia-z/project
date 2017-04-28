import django_filters
from django import template
register = template.Library()
from .models import Timeslot, Venue

class TimeslotFilter(django_filters.FilterSet):
    class Meta:
        model = Timeslot
        fields = ['venue', ]

class VenueFilter(django_filters.FilterSet):
    class Meta:
        model = Venue
        fields = {
        	'name': ['icontains', ],
        }

#date_range = DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}))