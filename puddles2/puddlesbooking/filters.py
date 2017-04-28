# Imports
import django_filters
from django import template
register = template.Library()

# App internal imports
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
