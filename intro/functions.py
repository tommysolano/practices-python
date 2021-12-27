def hello(name):
    print("hello " + name)

hello("world")
hello("joe")
hello("peter")

#####################

def add(numberOne, numberTwo):
    return numberOne + numberTwo

print(add(1, 2))

######################

add = lambda numberOne, numberTwo: numberOne + numberTwo

print(add(1, 2))
