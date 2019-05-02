import datetime

DAY, NIGHT = 1, 2
def check_time(time_to_check, on_time, off_time):
    if on_time > off_time:
        if time_to_check > on_time or time_to_check < off_time:
            return NIGHT, True
    elif on_time < off_time:
        if time_to_check > on_time and time_to_check < off_time:
            return DAY, True
    elif time_to_check == on_time:
        return None, True
    return None, False


on_time = datetime.time(23,30)
off_time = datetime.time(4,15)
timenow = datetime.datetime.now().time()
current_time = datetime.datetime.now().time()

when, matching = check_time(current_time, on_time, off_time)

if matching:
    if when == NIGHT:
        print("Night Time detected.")
    elif when == DAY:
        print("Day Time detected.")
