from django.shortcuts import render, redirect
from .models import Venue, Timeslot, Booking
from datetime import datetime, timedelta
import datetime
import operator
from .forms import PartySearchForm, BookingForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings


def home(request):
	'''
	Home page with search form
	Search for available time slots
	'''
	context ={'party_search_form' : PartySearchForm}
	template = "home.html"

	if request.method == 'GET':
		party_search_form = PartySearchForm(request.GET)

		if party_search_form.is_valid():

			# Store date input in session variable
			request.session['date_choice'] = str(party_search_form.cleaned_data['date']) 
			
			return redirect('availability/')

	return render(request, template, context)

def about(request):
	'''
	About us page
	Short business description
	'''
	context = {}
	template = "about.html"
	return render(request, template, context)

def venues(request):
	'''
	Short venues descrpiption
	Get each venue and display properties
	'''
	venue_list = Venue.objects.order_by('name')
	context = {'venue_list':venue_list}
	template = "venues.html"
	return render(request, template, context)

def availability(request):
	'''
	Display available timeslots for requested venue and date
	Get the date from session variable, get all bookings, 
	filter available timeslots against exiting bookings
	'''
	
	avail_timeslot_choices = []

	date = datetime.datetime.strptime(request.session['date_choice'], "%Y-%m-%d").date()

	bookings = Booking.objects.all().values_list('timeslot__id', flat=True).filter(date = date).filter(status = 'confirmed')

	avail_timeslot_choices = Timeslot.objects.filter(day_of_week = date.weekday()).exclude(id__in= bookings)

    # Contact us form prefilled with timeslot and date
	initial = "Please contact me in regards to the following: " + str("missing timeslot") + " " + str(date) #for modal, timeslot??????
	title = "Contact us"
	form = ContactForm(request.POST or None, initial={'comment': initial})
	confirm_message = None

	if form.is_valid():
		name = form.cleaned_data["name"]
		comment = form.cleaned_data["comment"]
		phone = form. cleaned_data["phone"]
		subject = 'Contact request'
		message = '%s %s %s' %(comment,name,phone)
		emailFrom = form.cleaned_data["email"]
		emailTo = [settings.EMAIL_HOST_USER, form.cleaned_data["email"]]

		send_mail(subject, message, emailFrom, emailTo, fail_silently = False)
		title = "Thanks!"
		confirm_message = "Thank you for contacting Puddles. We will get back to you within 72 hours"
		form = None

	context = {
		"title": title, 
		"form": form, 
		"confirm_message": confirm_message,
		'avail_timeslot_choices' : avail_timeslot_choices,
		'date' : date,
	}
	template = "availability.html"

	return render(request, template, context)


def booking(request):
	'''
	Get a quote form
	'''
	timeslot_id = request.GET.get('timeslot', '')
	timeslot = Timeslot.objects.get(id=timeslot_id)
	date = request.GET.get('date', '')
	
	title = "Get a quote"
	booking_form = BookingForm(request.POST or None, initial={'date':date})
	confirm_message = None

	if booking_form.is_valid():
		
		booking = booking_form.save(commit = False)
		booking.date = date
		booking.timeslot = timeslot
		booking.status = "SUBMITTED"
		booking.save()

		name = booking_form.cleaned_data["sname"]
		subject = 'New quote request'
		message = '%s %s' %(name,subject)
		emailFrom = booking_form.cleaned_data["email"]
		emailTo = [settings.EMAIL_HOST_USER, booking_form.cleaned_data["email"]]

		send_mail(subject, message, emailFrom, emailTo, fail_silently = False)
		title = "Thanks!"
		confirm_message = "Thank you for contacting Puddles. We will get back to you within 72 hours"
		form = None

	context = {'booking_form' : booking_form, 'timeslot' : timeslot, 'date' : date, "confirm_message": confirm_message,}
	template = "booking.html"

	return render(request, template, context)

# Contact form
def contact(request):
	'''
	Contact us form
	'''
	title = "Contact us"
	form = ContactForm(request.POST or None)
	confirm_message = None

	if form.is_valid():
		name = form.cleaned_data["name"]
		comment = form.cleaned_data["comment"]
		phone = form. cleaned_data["phone"]
		subject = 'Contact request'
		message = '%s %s %s' %(comment,name,phone)
		emailFrom = form.cleaned_data["email"]
		emailTo = [settings.EMAIL_HOST_USER]
		emailTo = form.cleaned_data["email"]

		send_mail(subject, message, emailFrom, emailTo, fail_silently = False)
		title = "Thanks!"
		confirm_message = "Thank you for contacting Puddles. We will get back to you within 72 hours"
		form = None
		
	context = {"title": title, "form": form, "confirm_message": confirm_message,}
	template = "contact.html"
	return render(request,template,context)