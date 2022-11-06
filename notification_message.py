from datetime import datetime
import pytz

def get_message():
    tz_LA = pytz.timezone('America/Los_Angeles') 
    datetime_LA = datetime.now(tz_LA)
    time_of_intrusion = "NY time:" + datetime_LA.strftime("%H:%M:%S")

    message = f"""\
    Subject: Intrusion Alert

    A drone entered your region of interest at \
    {time_of_intrusion}

    Drone Awareness notification service.
    """
    return message