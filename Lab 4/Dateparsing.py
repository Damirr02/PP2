import datetime
# Ex 1
print(datetime.datetime.now()-datetime.timedelta(days=5))
# Ex 2
print("Today: ", datetime.datetime.now())
print("Yesterday: ", datetime.datetime.now()-datetime.timedelta(days=1))
print("Tomorrow: ", datetime.datetime.now()+datetime.timedelta(days=1))
# Ex 3
current_datetime = datetime.datetime.now()
current_datetime_without_microseconds = current_datetime.replace(microsecond=0)
print("Datetime without microseconds:", current_datetime_without_microseconds)
# Ex 4
def diff(another_date):
    now = datetime.datetime.now()  
    days_diff = now.day - another_date
    return days_diff * 86400  
difference_seconds = diff(10)  
print(difference_seconds)