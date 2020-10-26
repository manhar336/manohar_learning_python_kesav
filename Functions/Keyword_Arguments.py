#Keyword Arguments :Keyword argument is a argument related to funtion calls ,caller identifies a argumnets by the parameter name
def name(firstname,middlename,lastname):
    'Keyword Arguments'
    print(firstname)
    print(middlename)
    print(lastname)
    return
name(firstname='Guido',middlename='Van',lastname='Rossum')
#name(firstname='Guido',middlename='Van') #TypeError: name() missing 1 required positional argument: 'lastname'

#The phrase Keyword Arguments are often shortened to kwargs in Python documentations