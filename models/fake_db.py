from models.event import *
from datetime import date



event1 = Events(date(2021,11,4), "RoS Codeclan Hangout", 16, "Brewdog", "RoS codeclan devs meeting with codeclan and RoS coaches plus Trev", False)
event2 = Events(date(2021,11,5), "RoS Codeclan Standup", 15, "Teams virtual", "RoS codeclan devs meeting with RoS coaches plus Trev & Daniel", True)
list_1 = [event1, event2]