from ics import Calendar, Event
import requests

new_cal_name = "busycal_export"
privacy = False

ext_ics_url = ""
ext_cal = Calendar(requests.get(ext_ics_url).text)

new_cal = Calendar()
new_cal.creator = new_cal_name # Defines PRODID

# Example Event to add to the Calendar
example_event = Event()
example_event.name = "Family Dinner Example Event"
example_event.begin = '2023-01-01 00:00:00'
new_cal.events.add(example_event)


# Add each event from the set of external calendar events to the new one
for event in ext_cal.events:

	if privacy == True:
		event.name = "Busy as a bee!"

	new_cal.events.add(event)


with open('%s.ics' % new_cal_name, 'w') as my_file:
    my_file.writelines(new_cal)