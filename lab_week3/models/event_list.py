from asyncio import events
from xmlrpc.client import FastUnmarshaller
from models.event import *

event_1 = Event("12/04/2022","Meeting", 8, "Meeting room 1","Party planning meeting",True)
event_2 = Event("23/08/2022","Festival", 100, "Main Stadium","Summer music festival",False)
event_3 = Event("12/12/2022","Birthday", 4, "Bar","Emma's 30th birthday", True)

events=[event_1, event_2,event_3]

def create_event(event):
    events.append(event)

