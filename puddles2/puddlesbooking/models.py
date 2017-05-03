# Imports
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

class PricePlan(models.Model):
	'''
	Base price plan
	'''
	name = models.CharField(max_length=120)
	description = models.TextField(null=False)
	price = models.DecimalField(max_digits=6, decimal_places=2)

	def __unicode__(self):
		return self.name

class Venue(models.Model):
	'''
	Venue Model
	'''
	name = models.CharField(max_length=120)
	description = models.TextField(null=False)
	address_1 = models.CharField(max_length=200, null=False)
	address_2 = models.CharField(max_length=200, null=True, blank=True)
	city = models.CharField(max_length=200, null=False)
	post_code = models.CharField(max_length=200, null=False)
	parking = models.CharField(max_length=120, null=False)
	group_min = models.IntegerField(default=5)
	group_max = models.IntegerField(default=25) 
	price_plans = models.ManyToManyField(PricePlan)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name

date_map = {
	5: "Saturday",
	6: "Sunday"
}
	
class Timeslot(models.Model):
	'''
	Timeslot Model
	'''
	WEEKDAY_CHOICES = (
    (5,'Saturday'),
    (6, 'Sunday'),
	)
	start_time = models.TimeField()
	end_time = models.TimeField()
	venue = models.ForeignKey(Venue, related_name="venue", null=False, on_delete=models.PROTECT, limit_choices_to={'active':True})
	day_of_week = models.IntegerField(null=False, choices=WEEKDAY_CHOICES)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.venue.name+" "+date_map[self.day_of_week]+" "+ self.start_time.strftime("%H:%M")


class Theme(models.Model):
	'''
	Theme Model
	'''
	name = models.CharField(max_length=30, null=False)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name


class AddOn(models.Model):
	'''
	Additions to the booking
	'''
	name = models.CharField(max_length=30, null=False)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name


class Booking(models.Model):
	'''
	Booking Model
	'''
	STATUS_CHOICES = (
    ('confirmed','CONFIRMED'),
    ('cancelled', 'CANCELLED'),
    ('submitted','SUBMITTED'),
    ('paid','PAID'),
	)

	SEX_CHOICES = (
    ('g', 'Girls'),
    ('b', 'Boys'),
    ('mix', 'Mix'),
	)

	DIETARY_CHOICES = (
    ('none', 'None'),
    ('veggie', 'Veggie'),
    ('vegan', 'Vegan'),
    ('halal', 'Halal'),
    ('kosher', 'Kosher'),
    ('no_chocolate', 'No chocolate coins'),
	)

	GROUP_SIZE_CHOICES = (
    ('xs', 'Up to 10'),
    ('s', '11 - 14'),
    ('m', '15 - 19'),
    ('l', '20 - 24'),
    ('xl', '25 - 30'),
	)

	'''
	Model
	'''
	date = models.DateField(null=False)
	timeslot = models.ForeignKey(Timeslot, null=True, on_delete=models.PROTECT)
	status = models.CharField(max_length=100, choices=STATUS_CHOICES)
	fname = models.CharField(max_length=100, null=False)
	sname = models.CharField(max_length=100, null=False)
	children_names = models.CharField(max_length=200, null=False)
	male_female = models.CharField(max_length=10, choices = SEX_CHOICES)
	children_ages = models.CharField(max_length=200, null=False)
	address_1 = models.CharField(max_length=200, null=False)
	address_2 = models.CharField(max_length=200, null=True, blank=True)
	city = models.CharField(max_length=200, null=False)
	post_code = models.CharField(max_length=200, null=False)
	email = models.EmailField(null=False)
	phone = models.CharField(max_length=20, null=False)
	number_of_children = models.CharField(max_length=10, choices = GROUP_SIZE_CHOICES)
	number_of_babies = models.PositiveIntegerField(null=True, blank=True)
	theme = models.ForeignKey(Theme, null=True, on_delete=models.PROTECT, limit_choices_to={'active':True})
	dietary_requirements = models.CharField(max_length=50, choices = DIETARY_CHOICES, null=True, blank=True)
	allergies = models.CharField(max_length=300, null=True, blank=True)
	flexible_dates  = models.BooleanField(default=True)
	#price_plan = models.ManyToManyField(AddOn)
	addons = models.ManyToManyField(AddOn, limit_choices_to={'active':True})
	other = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return str(self.timeslot)+" "+str(self.date)+" "+str(self.sname)

class Content(models.Model):
	'''
	Terms and Conditions Model
	'''
	name = models.CharField(max_length=30, null=False)
	text = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.name


class Unavailable(models.Model):
	'''
	Dates disabled from booking
	'''
	date = models.DateField(null=False)
	timeslots = models.ManyToManyField(Timeslot)

	def __unicode__(self):
		return str(self.date)