import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
now = datetime.datetime.now()

#task
year = 2017
month = 12
date = 4
hour = 9
min = 20

time_string = str(year)+"-"+str("%02d"%month)+"-"+str("%02d"%date)+" "+str("%02d"%hour)+":"+str("%02d"%min)
print(time_string)

print(type(now.year))
if year<now.year:
    print("past due")
if year>now.year:
    print("pending")
