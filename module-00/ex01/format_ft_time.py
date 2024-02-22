import time
import datetime

seconds_since_epoch = time.time()
scientific_notation = "{:.2e}".format(seconds_since_epoch)
formated_seconds = "{:,.4f}".format(seconds_since_epoch)
current_date = datetime.datetime.now().strftime("%b %d %Y")

print("Seconds since January 1, 1970:", scientific_notation, "or", formated_seconds, "in scientific notation")
print(current_date)