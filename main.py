from ics import Calendar, Event

cal_name = "Combined calendar export"

c = Calendar()
c.creator = cal_name # Defines PRODID

e = Event()
e.name = "Dinner with Mum"
e.begin = '2023-01-01 00:00:00'
c.events.add(e)

e2 = Event()
e2.name = "Dinner with Dad"
e2.begin = '2023-02-02 00:00:00'
c.events.add(e2)

c.events

with open('%s.ics' % cal_name, 'w') as my_file:
    my_file.writelines(c)