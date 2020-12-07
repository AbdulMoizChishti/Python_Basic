reward=int(input("Enter your reward="))
print("roll number= 022 , means we add 2200")
r=reward+2200
print("net amount after adding roll number=",r)
if reward>=20000 and reward<=34999 :
    print("Your Designation is organizer")
elif reward>=10000 and reward<=15000:
    print("Your Designation is Co-Organizer")
elif reward>=35000 and reward<=45000:
    print("Your Designation is Manager")
else:
    print("Your Designation is intern: negotiate")