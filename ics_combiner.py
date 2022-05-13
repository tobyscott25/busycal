from ics import Calendar, Event
import requests


def combine_ics(ics_urls):

	combined_calendar_name = "busycal_export"
	privacy = False

	combined_calendar = Calendar()
	combined_calendar.creator = combined_calendar_name # Defines PRODID

	# # Example Event to add to the Calendar
	# example_event = Event()
	# example_event.name = "Family Dinner (Example Event)"
	# example_event.begin = '2023-01-01 00:00:00'
	# combined_calendar.events.add(example_event)

	for ics_url in ics_urls:
		
		# Add each event from the set of external calendar events to the new one
		ext_cal = Calendar(requests.get(ics_url).text)
		for ext_event in ext_cal.events:

			# Remove possibly sensitive information if user wants privacy
			if privacy == True:
				ext_event.name = "Busy as a bee!" # Defines SUMMARY
				ext_event.description = ""
				ext_event.location = ""

			combined_calendar.events.add(ext_event)

	return combined_calendar