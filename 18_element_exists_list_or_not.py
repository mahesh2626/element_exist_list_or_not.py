n1=[int(x) for x in input('Enter some integer numbers:').split()]
f=int(input("Which element you want to find? :"))
for i in n1:
    if (f in n1):
        print("The Value",f,"is Found")
        break
    else:
        print("The Value",f,"is Not Found")
        break