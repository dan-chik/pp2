import calendar    
#printing the calendar of the year 2019    
s = calendar.prcal(2023)  

from datetime import date, timedelta
res = date.today() - timedelta(5)
print("Current date: ", date.today())
print("5 days before: ", res)
