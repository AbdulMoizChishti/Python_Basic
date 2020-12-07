#   Login page
import datetime
import random
pid=0
pname=""
fname=""
age=0
gn=""
print("\t\t Welcome to ABC Hospital Login Page")
id="admin"
password="admin"
if id == "admin" and password== "admin":
    print("\n\t\tWelcome")
    # Category
    print("\nplease select category\n")
    print("\t 1-Patient \n\t 2-Doctor ")
    choice=int(input("please select category:"))
    while choice !=4:
        if choice==1:
            todo=int(input("\n\t1-Admit \n\t2-Edit \n\t3-Discharge\n\tPlease Select any One:"))
            if todo==1:
                pid= random.random()*100
                pname=input("Enter Patient Name:")
                fname=input("Enter Father Name:")
                age=input("Enter Age:")
                gn=input("Enter Gender:")
                date = datetime.datetime.now()
                print("Time of admission:",date)
                ds= input("Enter Cause:")
                print("Patient name: ",pname,"fathername: ",fname,"age:  ",age, "gender: ",gn,"\n"  )
            elif todo==2:
                pname=input("Enter Patient Name:")
                fname=input("Enter Father Name:")
                age=input("Enter Age:")
                gn=input("Enter Gender:")
                print("Patient name: ",pname,"fathername: ",fname,"age:  ",age, "gender: ",gn,"\n"  )
            elif todo==3:
                pname=input("Enter Patient Name:")
                if pname== "moiz":
                    pname=""
                    fname=""
                    age=""
                    gn=""
                    ds=""
                    print("record has been removed")
                else:
                    print("record is mismatched")
            else:
                print("Time of admission:",date)
        else:         
                print("doctor module")
    
else:
    print("Invalid Id or Password")



