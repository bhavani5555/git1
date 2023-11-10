n=int(input("Enter n value\t"))
sum=0
for i in range(1,n):
    if i%2==1:
        sum+=i
        print("sum= ",sum)
