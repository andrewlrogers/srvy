import pandas as pd
import time
from datetime import datetime, date

start_date = date(2014, 1, 1)
end_date = datetime.now()
date_range = pd.date_range(start_date, end_date)

for date in date_range:
    print(date)
