#   Login page
import datetime
            
pname=""
fname=""
age=0
gn=""
print("\t\t Welcome to ABC Hospital Login Page")
id=(input("Enter ID:"))
password=(input("Enter password:"))
if id == "admin" and password== "admin":
    print("\n\t\tWelcome")
    # Category
    print("\nplease select category\n")
    print("\t 1-Patient \n\t 2-Doctor ")
    choice=int(input("please select category:"))
    if choice==1:
        todo=int(input("\n\t1-Admit \n\t2-Edit \n\t3-Discharge\n\tPlease Select any One:"))
        if todo==1:
            pname=input("Enter Patient Name:")
            fname=input("Enter Father Name:")
            age=input("Enter Age:")
            gn=input("Enter Gender:")
            date = datetime.datetime.now()
            print("Time of admission:",date)
            pr= input("Enter Cause:")
        elif todo==2:
               print("Time of admission:",date)
        else:
               print("Time of admission:",date)
    else:         
            print("doctor module")
    
else:
    print("Invalid Id or Password")


