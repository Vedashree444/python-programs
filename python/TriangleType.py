a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
c = int(input("enter value of c:"))

if((a or b or c) > 10):
    print("invalid entry")
    exit()
elif(a+b < c or b+c < a or a+c <b):
    print("triangle cannot be formed")
    exit()
if(a==b==c):
    print("equilateral triangle")
elif(a==b or b==c or c==a):
    print("isosceles triangle")
else:
    print("scalene triangle")

