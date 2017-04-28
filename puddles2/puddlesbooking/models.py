# Imports
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

class Venue(models.Model):
	'''
	Venue Model
	'''
	name = models.CharField(max_length=120)
	description = models.TextField(default="description default text")
	address_1 = models.CharField(max_length=200, null=False)
	address_2 = models.CharField(max_length=200, null=True, blank=True)
	city = models.CharField(max_length=200, null=False)
	post_code = models.CharField(max_length=200, null=False)
	parking = models.CharField(max_length=120, default="parking default text", blank=True, null=True)
	group_min = models.IntegerField(default=5)
	group_max = models.IntegerField(default=25) 
	catering = models.BooleanField(default=True)
	own_food = models.BooleanField(default=True)

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
    ('5','Saturday'),
    ('6', 'Sunday'),
	)
	start_time = models.TimeField()
	end_time = models.TimeField()
	venue = models.ForeignKey(Venue, related_name="venue", null=False, on_delete=models.CASCADE)
	day_of_week = models.IntegerField(null=False, choices=WEEKDAY_CHOICES)

	def __unicode__(self):
		return self.venue.name+" "+date_map[self.day_of_week]+" "+str(self.start_time)


class Theme(models.Model):
	'''
	Theme Model
	'''
	name = models.CharField(max_length=30, null=False)

	def __unicode__(self):
		return self.name


class AddOn(models.Model):
	'''
	Add-on Model
	'''
	name = models.CharField(max_length=200, null=False)
	price = models.DecimalField(max_digits=6, decimal_places=2)

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
	timeslot = models.ForeignKey(Timeslot, null=True)
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
	theme = models.ForeignKey(Theme, null=True, on_delete=models.CASCADE)
	dietary_requirements = models.CharField(max_length=50, choices = DIETARY_CHOICES, null=True, blank=True)
	allergies = models.CharField(max_length=300, null=True, blank=True)
	flexible_dates  = models.BooleanField(default=True)
	other = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return str(self.timeslot)+" "+str(self.date)+" "+str(self.sname)
'''
class BookingAddOn(models.Model):
	booking = models.ForeignKey(Booking, null=True, on_delete=models.CASCADE)
	add_on = models.ForeignKey(AddOn, null=True, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.id
'''

class TermsAndConditions(models.Model):
	'''
	Terms and Conditions Model
	'''
	name = models.CharField(max_length=30, null=False)
	text = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.name