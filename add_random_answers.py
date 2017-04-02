import pandas as pd
import time
from datetime import datetime, date
from random import randint

start_date = date(2014, 1, 1)
end_date = datetime.now()
date_range = pd.date_range(start_date, end_date)

for date in date_range:
    random_hour = randint(10, 17)
    random_minute = randint(0, 59)
    random_second = randint(0, 59)
    new_date = (date.year, date.month, date.day, random_hour, random_minute, random_second)
    print(new_date)
