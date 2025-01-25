# README: iCal Maker with Python

This project demonstrates how to create an iCalendar (.ics) file using Python. Follow the steps below to set up the environment, understand the code structure, and customize the demo data for your needs. U can start at step 4 if u don't want to have to start a vm everytime.

---

## Prerequisites

1. **Python 3** installed on your system (recommended: `/opt/homebrew/bin/python3`).
2. `icalendar` and `pytz` libraries installed.

---

## Step 1: Set Up a Virtual Environment

1. Navigate to your project directory:
   ```bash
   cd /path/to/Ical_Maker
   ```

2. Create a virtual environment:
   ```bash
   /opt/homebrew/bin/python3 -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

4. Install the required libraries:
   ```bash
   pip install icalendar pytz
   ```

---

## Step 2: Create the `school.py` Script

1. Create a file named `school.py` in your project directory.
2. Copy and paste the following template into `school.py`:

```python
from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz

# Define timezone
timezone = pytz.timezone("Europe/Brussels")

# Create a new calendar
cal = Calendar()
cal.add("prodid", "-//My Custom Timetable//EN")
cal.add("version", "2.0")

# Example: Replace with your data
events = [
    {"date": "YYYY-MM-DD", "start_time": "HH:MM", "end_time": "HH:MM", "class": "Event Name", "room": "Location"},
    {"date": "YYYY-MM-DD", "start_time": "HH:MM", "end_time": "HH:MM", "class": "Event Name", "room": "Location"},

    # Add more events here...
]

# Add events to the calendar
for event in events:
    start_dt = timezone.localize(datetime.strptime(f"{event['date']} {event['start_time']}", "%Y-%m-%d %H:%M"))
    end_dt = timezone.localize(datetime.strptime(f"{event['date']} {event['end_time']}", "%Y-%m-%d %H:%M"))

    cal_event = Event()
    cal_event.add("summary", event["class"])
    cal_event.add("location", event["room"])
    cal_event.add("dtstart", start_dt)
    cal_event.add("dtend", end_dt)
    cal.add_component(cal_event)

# Save the calendar to an .ics file
with open("timetable.ics", "wb") as f:
    f.write(cal.to_ical())

print("iCal file 'timetable.ics' generated successfully!")
```

---

## Step 3: Customize the Data

1. Open `school.py`.
2. Replace the placeholder data in the `events` list with your own timetable data. Example:

```python
events = [
    {"date": "2025-02-03", "start_time": "09:00", "end_time": "11:00", "class": "-T Communication", "room": "ELL.03.03"},
    {"date": "2025-02-03", "start_time": "11:00", "end_time": "13:00", "class": "-T .Net OOP", "room": "VIA.01.34"},
]
```

3. Save the file.

---

## Step 4: Run the Script

1. Ensure the virtual environment is active (you should see `(venv)` in your terminal prompt).
2. Run the script:
   ```bash
   python school.py
   ```
3. If successful, a file named `timetable.ics` will be generated in your project directory.

---

## Step 5: Deactivate the Virtual Environment

When you're done working on the project, deactivate the virtual environment:
```bash
deactivate
```

---

## Sample Data File

Below is a standalone Python script with demo data:

```python
from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz

# Define timezone
timezone = pytz.timezone("Europe/Brussels")

# Create a new calendar
cal = Calendar()
cal.add("prodid", "-//My Demo Timetable//EN")
cal.add("version", "2.0")

# Timetable data
events = [
    {"date": "2025-02-03", "start_time": "09:00", "end_time": "11:00", "class": "Sample Event 1", "room": "Room A"},
    {"date": "2025-02-03", "start_time": "11:00", "end_time": "13:00", "class": "Sample Event 2", "room": "Room B"},
]

# Add events to the calendar
for event in events:
    start_dt = timezone.localize(datetime.strptime(f"{event['date']} {event['start_time']}", "%Y-%m-%d %H:%M"))
    end_dt = timezone.localize(datetime.strptime(f"{event['date']} {event['end_time']}", "%Y-%m-%d %H:%M"))

    cal_event = Event()
    cal_event.add("summary", event["class"])
    cal_event.add("location", event["room"])
    cal_event.add("dtstart", start_dt)
    cal_event.add("dtend", end_dt)
    cal.add_component(cal_event)

# Save the calendar to an .ics file
with open("demo_timetable.ics", "wb") as f:
    f.write(cal.to_ical())

print("Demo iCal file 'demo_timetable.ics' generated successfully!")
```

---

Feel free to customize the data and share the `.ics` file with others!

Form Endy okpamen ode 
