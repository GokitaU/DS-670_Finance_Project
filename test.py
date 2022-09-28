import datetime

currentDate = datetime.date.today()
firstDayOfMonth = datetime.date(currentDate.year, currentDate.month, 1)

print(currentDate)
print(firstDayOfMonth)