"""
username = "Admin"
password = "12345"
attempt = 0
while attempt < 3:
    username = str(input("username:"))
    password = str(input("password:"))
    attempt = attempt +1
    if username == "Admin" and  password =="12345":
        print("Welcome :" +username)

    else:
        print("try again")

"""
#second method

attempt = 0
while attempt < 3:
    username = str(input("enter admin username:")).lower().strip()
    password = str(input("enter admin password")).strip()
    attempt = attempt +1
    if username == "admin" and password == "12345":
        print("Welcome to Python world:",username)
        break
    else:
        print("Please enter correct admin username and password within 3 attempts otherwise account will lock")

