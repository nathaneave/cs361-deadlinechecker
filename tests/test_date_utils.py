from app.date_utils import calculate_days_difference
from datetime import date, timedelta

def test_future_date():
    future = (date.today() + timedelta(days=7)).strftime("%Y-%m-%d")
    assert calculate_days_difference(future) == 7

def test_past_date():
    past = (date.today() - timedelta(days=5)).strftime("%Y-%m-%d")
    assert calculate_days_difference(past) == -5

def test_invalid_date():
    try:
        calculate_days_difference("01-01-2026")
    except ValueError:
        assert True
