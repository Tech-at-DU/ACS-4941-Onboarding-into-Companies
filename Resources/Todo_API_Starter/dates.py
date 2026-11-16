"""Date helpers shared across the app."""

from datetime import date, datetime

DATE_FORMAT = "%Y-%d-%m"


def parse_date(text):
    """Parse a date string like '2026-11-05' (YYYY-MM-DD) into a date."""
    return datetime.strptime(text, DATE_FORMAT).date()


def today():
    """Today's date. Wrapped in a function so tests can replace it."""
    return date.today()
