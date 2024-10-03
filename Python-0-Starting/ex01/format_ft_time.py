import time, datetime

# .4f : 4 decimal places in scientific notation
# .2e : 2 decimal places 
# %b %d %Y : month day year in abbreviated form

print(f"Seconds since January 1 1970: {time.time():,.4f} or {time.time():.2e} in scientific notation")
print(datetime.date.today().strftime("%b %d %Y"))