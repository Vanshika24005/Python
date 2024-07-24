a=input("enter first name:")
b=input("enter middle name:")
c=input("enter last name:")

while True:
    print("1. display full name :")
    print("2. exit :")
    ch=int(input("enter your choice:"))
    if ch==1:
        x=a.title()
        y=b.title()
        z=c[0].upper()
        print("Full Name:",x,y,z)
        break
    elif ch==2:
        break
    else:
        continue

