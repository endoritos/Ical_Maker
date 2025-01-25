from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz

# Timetable data
timetable = [
    {"date": "2025-02-03", "time": "09:00-11:00", "class": "-T Communication", "room": "ELL.03.03"},
    {"date": "2025-02-03", "time": "11:00-13:00", "class": "-T .Net OOP", "room": "VIA.01.34"},
    {"date": "2025-02-04", "time": "09:00-11:00", "class": "-T WEBPROG", "room": "ELL.01.08_1"},
    {"date": "2025-02-04", "time": "11:00-12:00", "class": "-T Analysis", "room": "ELL.01.08_1"},
    {"date": "2025-02-04", "time": "13:00-15:00", "class": "-L WEBPROG", "room": "ELL.01.08_1"},
    {"date": "2025-02-05", "time": "09:00-11:00", "class": "-L Analysis", "room": "ELL.03.09"},
    {"date": "2025-02-05", "time": "11:00-12:00", "class": "-T DATA STRUC", "room": "ELL.01.08_2"},
        {"date": "2025-02-06", "time": "09:00-11:00", "class": "-L REQ analysis", "room": "ELL.03.02"},
    {"date": "2025-02-06", "time": "11:00-13:00", "class": "-L NETOOP", "room": "ELL.03.02"},
        {"date": "2025-02-07", "time": "09:00-11:00", "class": "-L DAta Structures", "room": "ELL.01.08_3"},
    {"date": "2025-02-07", "time": "11:00-13:00", "class": "-L Intro Erp", "room": "ELL.01.08_3"},

    {"date": "2025-02-07", "time": "14:00-16:00", "class": "-T DBPROG", "room": "ELL.01.08_3"}
]

# Create an iCal calendar
cal = Calendar()
cal.add("prodid", "-//My Timetable//EN")
cal.add("version", "2.0")

# Convert timetable data into events
for entry in timetable:
    start_time, end_time = entry["time"].split("-")
    start_dt = datetime.strptime(f"{entry['date']} {start_time}", "%Y-%m-%d %H:%M")
    end_dt = datetime.strptime(f"{entry['date']} {end_time}", "%Y-%m-%d %H:%M")
    timezone = pytz.timezone("Europe/Brussels")
    start_dt = timezone.localize(start_dt)
    end_dt = timezone.localize(end_dt)

    event = Event()
    event.add("summary", entry["class"])
    event.add("location", entry["room"])
    event.add("dtstart", start_dt)
    event.add("dtend", end_dt)
    cal.add_component(event)

# Save to an .ics file
with open("timetable.ics", "wb") as f:
    f.write(cal.to_ical())

print("iCal file 'timetable.ics' generated successfully!")