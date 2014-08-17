import sys
import datetime

def get_day_of_week(derp):
    idx = derp.weekday()

    week_map = {
        0: "monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }

    day_name = week_map[idx]

    if day_name == "Monday":
        print("Ew, beginning of the week.")

    elif day_name == "Tuesday":
        print("You made it past Monday!")

    if idx > 2:
        print("Eico commercials are rad.")
    
