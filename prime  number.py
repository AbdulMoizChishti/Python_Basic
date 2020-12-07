ch=0
j=2
i=0
i=int(input("enter number"))
while (j<=i/2):
    if (i%j==0):
        print("It is not a prime number")
        ch=1
        break
    else:
        j=j+1
        if ch==0:
            print("its a prime number")
            break