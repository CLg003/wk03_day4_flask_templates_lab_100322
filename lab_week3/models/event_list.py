from asyncio import events
from models.event import *

event_1 = Event("12/04/1564","Meeting", 8, "Meeting room 1","Party plans")
event_2 = Event("23/08/2012","Festival", 100, "Main Stadium","Spring Break")
event_3 = Event("12/12/2022","Birthday", 4, "Bar","Emma birthday")

events=[event_1, event_2,event_3]

def create_event(event):
    pass