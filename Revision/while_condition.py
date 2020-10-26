"""
data = int(input("enter one number:"))
while data < 10:
    print("enter the data:",data)
    data = data +1
print("you are out of while loop:")
"""
password = ""
while password != 'redhat':
    password = input("please enter admin password:").strip().lower()
    if password == 'redhat':
        print("you entered admin correct password\t")
    elif password == 'admin123':
        print("you entered similar to admin password\t")
    elif password == 'linux123':
        print("you entered linux admin password\t")
    elif password:
        print("you entered wrong password\t")

print("you are outof while loop")
