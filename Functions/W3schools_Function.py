def myfunction(name):
    print(name +  ' Dharmala')
myfunction('Manohar')
myfunction('Deepika')
myfunction('Anshul')

#passing list as a parameter
#Creating a function
def myfunction(food):
    for vitamins in food:
        print("Healthy Food",vitamins)

#Creating a varible
fruits = ['apple','mango','grapes']
vegetables = ('Brinjal','Tomato')
#calling a function
myfunction(fruits)
print("")
myfunction(vegetables)

#Return values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))