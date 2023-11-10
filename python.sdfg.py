n=int(input("Enter n\t"))
f=n
while(f>=10):
    f//=10
    l=n%10
    sum=l+f
    print("sum= ",sum)
