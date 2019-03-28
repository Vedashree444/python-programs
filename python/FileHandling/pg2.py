def create():
    a = 1
    f = open("pg2 output", "a")
    usn = input("enter usn")
    name = input("enter name")
    college = input("enter college name")
    if (len(usn) > 10 or len(name) > 30 or len(college) > 10):
        print("invalid entry")
    else:
        line = usn +"|"+ name + "|"+college+"\n"
        f.write(line)
    f.close()

def read():
    f = open("pg2 output", "r")
    line =  f.read()
    print(line)
    f.close()

def search():
    f = open("pg2 output", "r")
    s = input("enter usn to be searched")
    i = True
    for x in f:
        res = x.split("|")
        x1 = x.split("-", 1)
        print("match found\n"+ x1[0])
        i = False
    if i:
        print("match not found")
    f.close()

def modify():
    b = 1
    f = open("pg2 output", "r+")
    usn = input("enter usn\n")
    while b == 1:
        pos = f.tell()
        res = f.readline().split("|")[0]
        if res == usn:
            f.seek(pos)
            name = input("enter name")
            college = input("enter college name")
            if (len(usn) > 10 or len(name) > 30 or len(college) > 10):
                print("invalid entry")
            else:
                line = usn + "|" + name + "|" + college + "\n"
                f.write(line)
                b = 0
    f.close()

b = 1
print("1.Insert\n2.Read\n3.Search\n4.Modify\n5.Exit")
while(b == 1):
    ch = int(input("enter choice\n"))
    if(ch == 1):
        create()
    elif(ch == 2):
        read()
    elif(ch==3):
        search()
    elif(ch==4):
        modify()
    elif(ch==5):
        b = 0
    else:
        b = 0