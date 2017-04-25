import datetime
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.core.validators import RegexValidator
from django.forms import ModelForm, Form

from .models import Venue, Booking, Theme


class PartySearchForm(forms.Form):
	'''
	Home page search form
	'''
	now = datetime.datetime.now()
	current_year = now.year
	date = forms.CharField(
		widget = forms.TextInput(
		attrs = {
			'id' : 'datepicker',
			'class' : 'datepicker',
		})
	)
	
class BookingForm(forms.ModelForm):
	'''
	Main booking form
	'''
	fname = forms.CharField(
		label = 'Your first name',
		widget = forms.TextInput(
		attrs = {
			'class': 'form-control',
		})
	)
	sname = forms.CharField(
		label = 'Your last name',
		widget = forms.TextInput(
		attrs = {
			'class': 'form-control',
		})
	)
	children_names = forms.CharField(
		label = "Your child(ren)'s name(s)",
		widget = forms.TextInput(
		attrs = {
			'class': 'form-control',
			'placeholder': 'Separated by commas (max 200 characters)',
		})
	)
	male_female = forms.ChoiceField(
		label = 'Boys or girls?', 
		choices = Booking.SEX_CHOICES,
		widget=forms.Select(
		attrs = {
			'class': 'form-control'
		})
	)
	children_ages = forms.CharField(
		label = "How old they will be after birthday?",
		widget = forms.TextInput(
		attrs = {
			'class': 'form-control',
			'placeholder': 'Separated by commas (max 200 characters)',
		})
	)
	address_1 = forms.CharField(
		widget = forms.TextInput(
		attrs = {
			'class': 'form-control',
			'placeholder': 'Address line 1',
		})
	)
	address_2 = forms.CharField(
		label = "Address line 2",
		widget = forms.TextInput(
		attrs = {
			'class': 'form-control',
			'placeholder': 'Address line 2',
		})
	)
	city = forms.CharField(
		label = "City",
		widget = forms.TextInput(
		attrs = {
			'class': 'form-control',
			'placeholder': 'City',
		})
	)
	post_code = forms.CharField(
		label = "Post code",
		widget = forms.TextInput(
		attrs = {
			'class': 'form-control',
			'placeholder': 'Post Code',
		})
	)
	email = forms.EmailField(
		widget = forms.TextInput(
		attrs = {
			'class': 'form-control',
		})
	)
	phone = forms.CharField(
		error_messages = {'invalid':"Enter a valid phone number."},
		validators=[RegexValidator('^(\+44\s?7\d{3}|\(?07\d{3}\)?)\s?\d{3}\s?\d{3}$')], 
		widget = forms.TextInput(
		attrs = {
			'class': 'form-control',
			'placeholder': 'e.g. 07712345678',
		})
	)
	number_of_children = forms.ChoiceField(
		choices = Booking.GROUP_SIZE_CHOICES,
		widget=forms.Select(
		attrs = {
			'class': 'form-control'
		})
	)
	number_of_babies = forms.IntegerField(
		required = False,
		label = "Estimated number of babies in arms/on laps not participating (under 1 year old):",
		widget=forms.NumberInput(
		attrs = {
			'class': 'form-control',
			'required': 'no'
		})
	)
	theme = forms.ModelChoiceField(
		queryset = Theme.objects.all(),
		widget=forms.Select(
		attrs = {
			'class': 'form-control'
		})
	)
	flexible_dates = forms.BooleanField(
		label= "Are your dates flexible?",
		widget=forms.CheckboxInput(
		attrs = {
			'class': 'form-control'
		})
	)
	#price plan
	dietary_requirements = forms.ChoiceField(
		choices = Booking.DIETARY_CHOICES,
		widget=forms.Select(
		attrs = {
			'class': 'form-control'
		})
	)
	allergies = forms.CharField(
		required = False,
		widget = forms.TextInput(
		attrs = {
			'class': 'form-control',
			'placeholder': 'max 200 characters',
		})
	)
	other = forms.CharField(
		required = False,
		widget = forms.Textarea(
		attrs = {
			'class': 'form-control',
			'placeholder': 'Add your comments here',
		})
	)
	class Meta:
		model = Booking
		fields = ['fname', 'sname', 'children_names', 'male_female', 'children_ages', 'address_1', 'address_2', 
		'city', 'post_code', 'email', 'phone', 'number_of_children', 'number_of_babies', 'theme',  
		'dietary_requirements', 'flexible_dates', 'allergies', 'other']

class ContactForm(forms.Form):
	'''
	Contact form
	'''

	name = forms.CharField(
		required=True, 
		max_length=100,
		label = 'Your name', 
		widget = forms.TextInput(
		attrs = {
			'class': 'form-control',
		})
	)
	phone = forms.CharField(
		error_messages = {'invalid':"Enter a valid phone number."},
		validators=[RegexValidator('^(\+44\s?7\d{3}|\(?07\d{3}\)?)\s?\d{3}\s?\d{3}$')], 
		widget = forms.TextInput(
		attrs = {
			'class': 'form-control',
			'placeholder': 'e.g. 07712345678',
		})
	)
	email = forms.EmailField(
		required=True,
		widget = forms.TextInput(
		attrs = {
			'class': 'form-control',
		})
	)

	comment = forms.CharField(
		required=True,
		widget = forms.Textarea(
		attrs = {
			'class': 'form-control',
			'placeholder': 'Add your comments here',
		})
	)