from datetime import datetime
current = datetime.now()
current_datetime_str = current.strftime('%A, %B %d, %Y')
print("Today is {}".format(current_datetime_str))
