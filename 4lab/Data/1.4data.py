import datetime

date1 = input("(YYYY-MM-DD HH:MM:SS): ")         #for example: 2006-02-12 10:02:05
date2 = input("(YYYY-MM-DD HH:MM:SS): ")         #Так нельзя: 2006 02 12 10 02 05

dt1 = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
dt2 = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")

diff_seconds = abs((dt2 - dt1).total_seconds())

print(f"difference: {int(diff_seconds)}")

