from asyncio import events
from xmlrpc.client import FastUnmarshaller
from models.event import *

event_1 = Event("12/04/1564","Meeting", 8, "Meeting room 1","Party plans",True)
event_2 = Event("23/08/2012","Festival", 100, "Main Stadium","Spring Break",False)
event_3 = Event("12/12/2022","Birthday", 4, "Bar","Emma birthday", True)

events=[event_1, event_2,event_3]

def create_event(event):
    events.append(event)

