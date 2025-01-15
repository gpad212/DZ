#Zadanie 1
from datetime import datetime, timedelta

date_1 = datetime(2002,10,2)
date_2 = datetime(2013,11,10)
date_3 = datetime(1977,8,18)

print("The Moscow Times - " + date_1.strftime("%A, %B %d,%Y"))
print("The Guardian - " + date_2.strftime("%A, %m.%d.%y"))
print("Daily News - " + date_3.strftime("%A, %d %B %Y"))


#Zadanie 2

def date_range(start_date,end_date):
    all_date = []
    if start_date > end_date:
        print(f"date_range ('{start_date.strftime("%Y-%m-%d")}', '{end_date.strftime("%Y-%m-%d")}')")
        print(all_date)
    else:
        print(f"date_range ('{start_date.strftime("%Y-%m-%d")}', '{end_date.strftime("%Y-%m-%d")}')")
        all_date.append(start_date.strftime("%Y-%m-%d"))
        while start_date < end_date:
            start_date += timedelta(days=1)
            all_date.append(start_date.strftime("%Y-%m-%d"))

        print(all_date)

start_date = datetime(2002,10,2)
end_date = datetime(2002,10,10)

date_range(start_date,end_date)
