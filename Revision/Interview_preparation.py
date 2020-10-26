#finding out min number
def sum(number):
    if len(number)==1:
        return number[0]
    else:
        return number[0] + sum(number[1:])


test = [1,2,3,4]
print(sum(test))

def min_element(a):
    if len(a)==1:
        return a
    else:
        return a
test1= [1,2,3,4]
print(max(test1))