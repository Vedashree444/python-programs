locks = int(input("enter number of locks:"))
stocks = int(input("enter number of stocks:"))
barrels = int(input("enter number of barrels"))
if ((locks <= 0) or (locks > 70) or ((stocks <= 0) or (stocks > 80)) or((barrels <= 0) or (barrels > 90))):
    print("invalid input")
    exit()

sales = locks*45 +stocks*30 + barrels*25

if(sales<=1000):
    commission = sales*0.1
elif(sales > 1000 or sales<=1800):
    commission = 1000*0.1 + (sales-1000)*0.15
else:
    commission = 1000*0.1 +800*0.15 +(sales-1800)*0.20

print("sales : "+str(sales))
print("commission : "+str(commission))