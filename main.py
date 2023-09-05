# Email send Bot for Daily Sayings
# Version 2.0
# Copyright 2023 by Holger Hunger

# Sends daily sayings from various sources to email recipients stored in a mariadb database on each call.


import datetime as dt
from database import get_mail_list

# Get the day of the week
# Monday is 0 and Sunday is 6 (source: docs.python.org)
now = dt.datetime.now()
dayOfWeek = now.weekday()
dayOfWeek = 6

# Get Email Address List
receiver_list = get_mail_list(dayOfWeek)
print(receiver_list)
# If Email List Empty > Quit
# if

# Get Quote or Advice

# Send Quote to Email List
