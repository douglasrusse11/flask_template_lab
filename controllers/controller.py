from flask import render_template, request, redirect
from our_app import our_app
from models.fake_db import *
from models.event import Events
from datetime import date, datetime

print(Events)

@our_app.route('/')
def index():
    return render_template('index.html', events = "Upcoming Events", my_events = list_1) 

@our_app.route('/', methods=["POST"])
def create_event():
    print(request.form)
    submitted_date = request.form["Date"]
    year = int(submitted_date[0:4])
    month = int(submitted_date[5:7])
    day = int(submitted_date[8:10])
    event_date = date(year, month, day)
    # event_date = datetime.strptime(request.form["Date"], "%Y-%m-%d").date()
    name = request.form["Name"]
    guests_num = request.form["Number of Guests"]
    room_location = request.form["Room Location"]
    description = request.form["Description"]
    if "Recurring" in request.form:
        recurring = True
    else:
        recurring = False
    new_event = Events(event_date, name, guests_num, room_location, description, recurring)
    list_1.append(new_event)
    return redirect('/')

@our_app.route('/events/delete/<index>', methods=['POST'])
def delete_event(index):
    list_1.pop(int(index))
    return redirect('/')