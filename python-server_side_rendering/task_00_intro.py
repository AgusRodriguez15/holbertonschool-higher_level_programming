import os

def generate_invitations(template, attendees):
    if isinstance(template, str): 
        raise TypeError("template must be a string")
    
    if isinstance(attendees, list):
        raise TypeError("attendees must be a list")
    
    if template == "":
        raise ValueError("template is empty")
    
    if attendees == "":
        raise ValueError("attendees is empty")