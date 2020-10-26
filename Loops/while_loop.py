"""
Python Loops

1. for
2. while is based on True or false condition

The while loop: with the while loop we can execute a set of statements as long as a condition is true
while is always check true condition ,if its True it will execute until encounter condition is false(if its false program will terminate) else it it infinity loop

while syntax
while expression:
    statement

"""
data = 1
while data < 8:   #while is keyword
    print(data)   #it will keep on printing because it will terminate when the program is false statement
    data +=1      #first iteration 1+1=2 ,second iteration 2+1=3,third iteration 3+1=4,fourth iteration 4+1=5 it will print upto condition false
print("Out of while block")
print("----------------------------------")

data = 1
while data > 8:   #Here while condition is false ,so wont execute statements
    print(data)
    data +=1
print("Out of while block")

print("-----------------------------")
data = 1
while data < 8:
    print(data)
    data +=1
    if data == 5:  #once data reaches 5 and it will break the program
        break
print("Out of while block")