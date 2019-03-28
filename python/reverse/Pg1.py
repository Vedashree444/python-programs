print("1.Standard I/O \n2.User I/O")
choice = int(input("enter your choice"))

if choice==1:
    n = int(input("Enter the number of names : "))
    for i in range(0,n):
        s = str(input("Enter a name : "))
        print(s[::-1])

elif choice==2:
    fp1 = input("enter input file name\n")
    fp2 = input("enter output file name\n")
    fi = open(fp1 , "r")
    fo = open(fp2 , "w")
    for x in fi:
        fo.write(x.strip()[::-1]+"\n")

else:
    print("invalid choice\n")


