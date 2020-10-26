#Note:part of elif we can check multiple expressions and conditions
#Note:suppose if condition fails then go to elif condition if again fails then go to next elif condition
course = input("what course are you doing ")

if course == "python":
    print("you are doing python course and do more practise")
elif course == "java":
    print("you are doing Java course and do more examples")
elif course == "DevOps":
    print("You will become Devops engineer")
else:
    print("you are already completed courses and gennious")
print("you are not doing any course")
print("----------------------------------")

value = 100
if value > 200: #Here condition is false
    print("this is in block-1")
elif value >=200: #Here condition is false
    print("this is block-2")
elif False:
    print("this is block-3")
elif True:        #Here True is Key Word
    print("this is correct")
else:
    print("this is final block")


