import datetime, calendar

balance = 5000
interest = 13 * 0.01
monthly = 500

today = datetime.date.today()
day = calendar.monthrange( today.year, today.month )[1]
end = day - today.day

start = today + datetime.timedelta(days=end+1)
print(start)

print( day ) 
print(end)
