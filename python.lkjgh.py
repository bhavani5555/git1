n=int(input("Enter n"))
m=n
rev=0
while (n>0):
    t=n%10
    rev=rev*10+t
    n=n//10
    if (m==rev):
        print("Given n is palindrome\n")
    else:
            print("Given n is not palindrome\n")
