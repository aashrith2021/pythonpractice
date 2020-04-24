from datetime import datetime,timedelta
today=datetime.now()
print(today) 
print
print(today.year)
print
print(today.day)
print
print(today.month)
#timedelta - used for going back from a specific date
oneday=(timedelta(days=2))
print(today-oneday)
#strptime used for date format
bday=input('enter birth day')
birth=datetime.strptime(bday,'%d/%m/%Y')
print(birth)

