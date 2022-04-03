from datetime import datetime, timedelta

def get_last_days(n):
    today = datetime.now()
    days = []
    for k in range(n):
        delta = timedelta(days=k)
        day = today - delta
        days.append(day)
    return days

DATE_FORMAT = "%m/%d/%Y"

def date_format_to_string(date: datetime):
    return date.strftime(DATE_FORMAT)

def string_to_date_format(date: str):
    return datetime.strptime(date, DATE_FORMAT)