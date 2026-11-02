roles=['user','admin','staff']
role =input("enter your role:")

if role not in roles:
    print("Invalid role. Please enter a valid role.")
