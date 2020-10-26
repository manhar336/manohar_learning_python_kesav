mac_os = 300

if mac_os < 200:
    print("you are less than 200")
    if mac_os < 150:
        print("you are less than 150")
    elif mac_os < 100:
        print("your number less than 100")
    else:
        print("your number is more")
elif mac_os > 200:
    print("you are greater than 100")
    if mac_os == 40:
        print("you are in 40")
    elif mac_os > 300:
        print("you are less than 300")
    else:
        print("you are more number")

else:
    print("you are done")
