#!/usr/bin/python3
"this file is for try and undertand how to do"

attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

#template = "Hello {name}, You are invited to the {event_title} on {event_date} at {event_location}. We look forward to your presence. Best regards, Event Team"
with open('template.txt','r') as file:
    text = file.read()

 
for attendee in attendees:
    replace = text.format(
      name=attendee.get("name", "N/A"),
      event_title=attendee.get("event_title", "N/A"),
      event_date=attendee.get("event_date", "N/A") if attendee["event_date"] else "N/A",
      event_location=attendee.get("event_location", "N/A")
    )
    print(replace)
    
