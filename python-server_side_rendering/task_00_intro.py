import os

def generate_invitations(template, attendees):
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