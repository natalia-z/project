# Django imports
from datetime import datetime, timedelta
import datetime
import operator
#import requests
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect


# App internal imports
from .models import Venue, Timeslot, Booking, Unavailable
from .forms import PartySearchForm, BookingForm, ContactForm
from .filters import TimeslotFilter, VenueFilter


def home(request):
	'''
	Search for available time slots
	'''
	if request.method == 'GET':
		party_search_form = PartySearchForm(request.GET)

		if party_search_form.is_valid():

			# Store date input in session variable
			request.session['date_choice'] = str(party_search_form.cleaned_data['date']) 
			
			return redirect('availability/')

	# Template, context
	template = "home.html"
	context ={
		'party_search_form' : PartySearchForm
	}

	return render(request, template, context)

def about(request):
	'''
	About us page
	'''
	template = "about.html"
	context = {}

	return render(request, template, context)

def venues(request):
	'''
	Venues descrpiption
	'''
	venue_list = Venue.objects.all()
	venue_filter = VenueFilter(request.GET, queryset=venue_list)

	# Template, context
	template = "venues.html"
	context = {
		'venue_list' : venue_list,
		'filter' : venue_filter
	}

	return render(request, template, context)

def availability(request):
	'''
	Display available timeslots for requested venue and date
	Get the date from session variable, get all bookings, 
	get disabled dates, filter available timeslots against 
	exiting bookings and disabled dates
	'''
	
	date = datetime.datetime.strptime(request.session['date_choice'], "%Y-%m-%d").date()

	bookings = Booking.objects.all().values_list('timeslot__id', flat=True).filter(date = date).filter(status = 'confirmed')

	unavailable = Unavailable.objects.all().values_list('timeslots__id', flat=True).filter(date = date)
	
	avail_timeslot_choices = Timeslot.objects.filter(day_of_week = date.weekday()).exclude(id__in = bookings).exclude(id__in = unavailable).exclude(active=False)

	timeslot_filter = TimeslotFilter(request.GET, queryset=avail_timeslot_choices)

	message = None

	if len(avail_timeslot_choices) < 1:
		message = "Oops, looks like we're fully booked. Try another date."

    # Contact us form prefilled with timeslot and date
	initial = "Please contact me in regards to the following: [timeslot] " + str(date)
	title = "Contact us"
	form = ContactForm(request.POST or None, initial={'comment': initial})
	confirm_message = None

	if form.is_valid():
		ccme_contact = form.cleaned_data["ccme_contact"]
		name = form.cleaned_data["name"]
		comment = form.cleaned_data["comment"]
		phone = form. cleaned_data["phone"]
		subject = 'Contact request'
		message = '%s %s %s' %(comment,name,phone)
		message2 = 'Thank you for contacting us. The following message has been sent to Puddles: You have a new contact request: %s | %s | %s' %(name,phone, comment)
		emailFrom = form.cleaned_data["email"]
		emailTo = [settings.EMAIL_HOST_USER,]
		emailTo2 = [form.cleaned_data["email"],]


		if ccme_contact == True:
			send_mail(subject, message, emailFrom, emailTo, fail_silently = False)
			send_mail(subject, message2, emailFrom, emailTo2, fail_silently = False)
		else:
			send_mail(subject, message, emailFrom, emailTo, fail_silently = False)
			
		title = "Thanks!"
		confirm_message = "Thank you for contacting Puddles. We will get back to you within 72 hours"
		return HttpResponseRedirect('/availability/')
		

	# Template, context
	template = "availability.html"
	context = {
		"title": title, 
		"form": form, 
		"confirm_message": confirm_message,
		'avail_timeslot_choices' : avail_timeslot_choices,
		'date' : date,
		'message' : message,
		'filter': timeslot_filter,
	}

	return render(request, template, context)


def booking(request,id,date):
	'''
	Get a quote form
	'''
	'''
	timeslot_id = request.GET.get('timeslot', '')
	print(timeslot_id)
	timeslot = Timeslot.objects.get(id=timeslot_id)
	print (timeslot)
	date = request.GET.get('date', '')
	'''
	timeslot = Timeslot.objects.get(id=id)
	date = date
	title = "Get a quote"
	booking_form = BookingForm(request.POST or None, initial={'date':date})
	confirm_message = None	

	if booking_form.is_valid():
		
		booking = booking_form.save(commit = False)
		booking.date = date
		booking.timeslot = timeslot
		booking.status = "submitted"
		booking.save()
		booking_id = booking.id

		ccme = booking_form.cleaned_data["ccme"]
		fname = booking_form.cleaned_data["fname"]
		sname = booking_form.cleaned_data["sname"]
		subject = 'New quote request'
		message = 'You have a new quote request from %s %s for %s on %s . See the request: https://puddlesbooking.herokuapp.com/admin/puddlesbooking/booking/%s/change/' %(fname,sname,timeslot,date, booking_id)
		message2 = 'Thank you for submitting your request. The following message has been sent to Puddles: You have a new quote request from %s %s for %s on %s.' %(fname,sname,timeslot,date)
		emailFrom = booking_form.cleaned_data["email"]
		emailTo = [settings.EMAIL_HOST_USER,]
		emailTo2  = [booking_form.cleaned_data["email"],]		

		if ccme == True:
			send_mail(subject, message, emailFrom, emailTo, fail_silently = False)
			send_mail(subject, message2, emailFrom, emailTo2, fail_silently = False)
		else:
			send_mail(subject, message, emailFrom, emailTo, fail_silently = False)

		title = "Thanks!"
		confirm_message = "Thank you for contacting Puddles. We will get back to you within 72 hours"
		form = None
		
	# Template, context
	template = "booking.html"
	context = {'booking_form' : booking_form, 'timeslot' : timeslot, 'date' : date, 'confirm_message' : confirm_message, 'title' : title}
	
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
		ccme_contact = form.cleaned_data["ccme_contact"]
		name = form.cleaned_data["name"]
		comment = form.cleaned_data["comment"]
		phone = form. cleaned_data["phone"]
		subject = 'Contact request'
		message = 'You have a new contact request: %s | %s | %s' %(name,phone, comment)
		message2 = 'Thank you for contacting us. The following message has been sent to Puddles: You have a new contact request: %s | %s | %s' %(name,phone, comment)
		emailFrom = form.cleaned_data["email"]
		emailTo = [settings.EMAIL_HOST_USER,]
		emailTo2 = [form.cleaned_data["email"],]

		if ccme_contact == True:
			send_mail(subject, message, emailFrom, emailTo, fail_silently = False)
			send_mail(subject, message2, emailFrom, emailTo2, fail_silently = False)
		else:
			send_mail(subject, message, emailFrom, emailTo, fail_silently = False)

		title = "Thanks!"
		confirm_message = "Thank you for contacting Puddles. We will get back to you within 72 hours"
		form = None
		
	# Template, context
	template = "contact.html"
	context = {"title": title, "form": form, "confirm_message": confirm_message,}

	return render(request,template,context)