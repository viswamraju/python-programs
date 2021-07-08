from datetime import *
import pytz


def get_current_time():
    tz_INDIA = pytz.timezone('Asia/Kolkata')
    datetime_INDIA = datetime.now(tz_INDIA)
    print(datetime_INDIA.strftime("%H:%M:%S"))


def present_future_date():
    current_date = datetime.now()
    previous_date = current_date - timedelta(1)
    future_date = current_date + timedelta(1)

    print(future_date, current_date, previous_date)


present_future_date()