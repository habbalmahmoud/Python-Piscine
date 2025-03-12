from datetime import date
import time
months = date.today().month

years = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]

timestamp = time.time()

formatted = f"{timestamp:,.4f}"

sci = f"{timestamp:.2e}"

print ("Seconds since January 1, 1970: "+formatted+" or "+sci+" in scientific notation")

month = years[months - 1]
year = date.today().year
day = date.today().day
print(month, day, year)
