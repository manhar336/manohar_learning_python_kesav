name = input("enter your name:")
print("welcome to the game:",name)
age = int(input("enter your age:"))
color_selection = input("select color which you want to choose:").lower()

if age < 15:
    if color_selection == "blue":
        print("you are first in the game:")
    elif color_selection == "yellow":
        print("yellow yellow dirty fellow")
    elif color_selection == "red":
        print("you selected dangerours color")
    else:
        print("selected color not their in the game")


else:
    print("you are not eligible to play the game:")
