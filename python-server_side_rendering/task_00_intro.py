#!/usr/bin/python3

def generate_invitations (template, attendees):
    
    if isinstance(template, str): 
        print("error: template must be a string")
        return
    
    if isinstance(attendees, list):
        print("error: attendees must be a list")
        return
    
    if not template:
        print("error: template is empty")
        return
    
    if not attendees:
        print("error: attendees is empty")
        return
    
    with open('template.txt','r') as file:
        text = " ".join(line.rstrip() for line in file)

    with open('output_1.txt', 'w') as output_file:
        for attendee in attendees:
            replace = text.format(
                name=attendee.get("name", "N/A"),
                event_title=attendee.get("event_title", "N/A"),
                event_date=attendee.get("event_date", "N/A") if attendee["event_date"] else "N/A",
                event_location=attendee.get("event_location", "N/A")
            )
            output_file.write(replace + "\n")
    print(replace)
    