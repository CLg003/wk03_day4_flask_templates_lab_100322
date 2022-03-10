from crypt import methods
from operator import methodcaller
from flask import render_template, request
from app import app
from models.event_list import events, create_event
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title="Home", events=events)
    
@app.route('/events', methods=['POST'])
def add_event():
    event_name = request.form['name']
    event_date = request.form['date']
    event_location = request.form['location']
    event_description = request.form['description']
    event_guest = request.form['guest']
    event_recurring= True if "recurring" in request.form else False
    new_event = Event(event_date,event_name,event_guest,event_location,event_description,event_recurring)
    create_event(new_event)

    return render_template('index.html', title="Home", events=events)
