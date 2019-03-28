date = int(input("enter date"))
month = int(input("enter month"))
year = int(input("enter year"))
if(date < 1 or date > 31)or(month < 1 or month > 12)or(year < 1812):
    print("invalid entry")
    exit()
tirty = [4,6,9,11]
tirtyone = [1,3,5,7,8,10,12]

if(month in tirty):
    if(date < 30):
        date = date +1
    elif(date==30):
        date = 1
        month = month +1

elif(month in tirtyone):
    if(month == 12 and  date == 31):
        year = year +1
        date = 1
        month = 1
    elif(date < 31):
        date = date+1
    elif(date==31):
        date = date+1
        month = month+1
else:
    if(date > 30):
        print("invalid date")
    elif(year%4==0):
        if(date == 29 ):
            month = month + 1
            date = 1
        if(date < 29):
            date = date + 1
    else:
        if(date < 28):
            date = date + 1
        elif(date==28):
            date = 1
            month = month +1
print(str(date)+" \ "+str(month)+" \ "+str(year))
