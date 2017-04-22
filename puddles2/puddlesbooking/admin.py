from django.contrib import admin

# Register your models here.
from .models import Venue, Timeslot, Theme, Booking

class VenueModelAdmin(admin.ModelAdmin):
	list_display = ["name", "city", "post_code"]
	list_filter = ["catering", "own_food", "city", "post_code"]
	search_field = ["name", "city"]
	class Meta:
		model = Venue

class TimeslotModelAdmin(admin.ModelAdmin):
	list_display = ["venue", "day_of_week", "start_time", "end_time"]
	list_filter = ["venue", "day_of_week", "start_time", "end_time"]
	search_field = ["venue", "day_of_week", "start_time", "end_time"]
	class Meta:
		model = Timeslot

class BookingModelAdmin(admin.ModelAdmin):
	list_display = ["get_venue_name", "get_start_time","get_end_time", "date", "get_day_of_week", "sname", "status"]
	list_filter = ["timeslot__venue", "timeslot__start_time","timeslot__end_time", "date", "timeslot__day_of_week", "sname", "status"]
	#search_field = ["get_venue_name", "get_start_time","get_end_time", "date", "get_day_of_week", "sname", "status"]
	class Meta:
		model = Booking

	def get_day_of_week(self, obj):
		return obj.timeslot.day_of_week
	get_day_of_week.short_description = 'Day of the week' 
	get_day_of_week.admin_order_field  = 'timeslot__day_of_week'

	def get_start_time(self, obj):
		return obj.timeslot.start_time
	get_start_time.short_description = 'Start time' 
	get_start_time.admin_order_field  = 'timeslot__start_time'

	def get_end_time(self, obj):
		return obj.timeslot.end_time
	get_end_time.short_description = 'End time' 
	get_end_time.admin_order_field  = 'timeslot__end_time'

	def get_venue_name(self, obj):
		return obj.timeslot.venue
	get_venue_name.short_description = 'Venue name' 
	get_venue_name.admin_order_field  = 'timeslot__venue'

admin.site.register(Venue, VenueModelAdmin)
admin.site.register(Timeslot, TimeslotModelAdmin)
admin.site.register(Booking, BookingModelAdmin)
admin.site.register(Theme)