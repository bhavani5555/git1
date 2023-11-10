n=int(input("enter n\t"))
f=n
while(f>=10):
    f//=10
    l=n%10
    print("First digit= ",f)
    print("Last digit= ",l)
