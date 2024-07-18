import time, datetime

print(f"Seconds since January 1 1970: {format(time.time(), ',.4f')} or {format(time.time(), '.2e')} in scientific notation")
print(datetime.date.today().strftime("%b %d %Y"))