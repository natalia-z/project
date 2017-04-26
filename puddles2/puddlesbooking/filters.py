import django_filters
from .models import Timeslot

class TimeslotFilter(django_filters.FilterSet):
    class Meta:
        model = Timeslot
        fields = ['venue', ]