password = ""
while password !="redhat":
    password = input("Please enter your password:")
    if password == "redhat":
        print("you entered redhat correct  password")
    elif password == "admin@123":
        print("It was previously used password")
    elif password == "admin":
        print("This is alerady used password")
    else:
        print("you entered wrong password")
print("Out of while block")
'''
Note :if we condition  match then while loop will proceed ,if we enter admin@123 program will execurte and iteration repeat 
if we enter password as redhat means  condition false and program will terminate 


'''