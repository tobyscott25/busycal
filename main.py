from ics import Calendar, Event
import requests

new_cal_name = "busycal_export"
privacy = True


new_cal = Calendar()
new_cal.creator = new_cal_name # Defines PRODID

# Example Event to add to the Calendar
example_event = Event()
example_event.name = "Family Dinner (Example Event)"
example_event.begin = '2023-01-01 00:00:00'
new_cal.events.add(example_event)


# Array of .ics and .ical URLS to include in the export
ext_ics_urls = []

for ics_url in ext_ics_urls:
	
	# Add each event from the set of external calendar events to the new one
	ext_cal = Calendar(requests.get(ics_url).text)
	for ext_event in ext_cal.events:

		# Remove possibly sensitive information if user wants privacy
		if privacy == True:
			ext_event.name = "Busy as a bee!" # Defines SUMMARY
			ext_event.description = ""
			ext_event.location = ""

		new_cal.events.add(ext_event)




with open('%s.ics' % new_cal_name, 'w') as export_file:
    export_file.writelines(new_cal)