rate=0
rate1=0
fl=""
print("\t Welcome to the pizza shop\n")
print("\t\t Category: \t\t Flavours:")
print("\t   1-small - 300 rs \t\t 1- bbq \n\t   2-regular - 500 rs \t\t 2- fajita \n\t   3-large - 700 rs \t\t 3- afghani \n")

print("\t How may I help you?\n")
qty=int(input("Enter QTY"))


size=int(input("Enter Size"))
f=int(input("Enter FlAVOUR"))
while(size>3):
    if size==1:
        rate=300
    elif size==2:
        rate=500
    elif size==3:
        rate=700
while(f>3):    
    if f==1:
        fl="bbq"
    elif f==2:
        fl="fajita"
    elif f==3:
        fl="afghani"    
    
print("\t\t 1- Extra cheese- 40 rs \n\t\t 2-extra ketchup- 60 rs \n\t\t 3- none")
top=int(input("enter your topping"))
while(top>3):
    if top==1:
        rate1=40
    elif top==2:
        rate1=60
      
price=qty*(rate1+rate)
print("total price",price)