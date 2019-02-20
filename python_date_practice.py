#Working with the datetime module
from datetime import datetime

now = datetime.now()
utc_now = datetime.utcnow()

#The function below can likely be found in the datetime module
def date_diff(date1,date2):
    return date1 - date2

print(now)
print(utc_now)
print(date_diff(now,utc_now))
