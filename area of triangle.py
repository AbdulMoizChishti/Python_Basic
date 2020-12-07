a=int(input("Enter any value ="))
b=int(input("Enter any value ="))
c=int(input("Enter any value ="))
s=(a+b+c)/2
d=(s*(s-a)*(s-b)*(s-c))
area=(d**0.5)
print("The area of triangle is =",round(area,3))