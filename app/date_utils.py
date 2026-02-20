from datetime import datetime, date

def calculate_days_difference(event_date: str) -> int:
    provided_date = datetime.strptime(event_date, "%Y-%m-%d").date()
    today = date.today()
    return (provided_date - today).days
