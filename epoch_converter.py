"""Converts a given date (UTC) into timestamp (in seconds) and copy the result to the clipboard"""
import datetime
import sys
import pyperclip

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        date = str(datetime.datetime.utcnow().date())
    else:
        date = sys.argv[1]
    y, m, d = list(map(int, date.split("-")))
    dt = datetime.datetime(y, m, d)
    unix_ts_utc = int(dt.replace(tzinfo=datetime.timezone.utc).timestamp())
    print(unix_ts_utc)
    pyperclip.copy(unix_ts_utc)
