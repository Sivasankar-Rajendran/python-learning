# PYTHON VARIABLES:

# Variables:
# Variables are containers for storing data values.

# A variable is created the moment you first assign a value to it.
x = 5
y = "Hello, World!"
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
a = 4       # a is of type int
a = "Sally" # a is now of type str
print(a)

# Casting: If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

# Get the type: You can get the data type of a variable with the type() function.
x = 10
print(type(x))
x = "Hello"
print(type(x))

# Single or Double Quotes? String variables can be declared either by using single or double quotes:
x = "John" 
x = 'John'

# Case-Sensitive - Variable names are case-sensitive.
a = 10
A = 20
print(a)   
print(A)

# PYTHON VARIABLE NAMES:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"    
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"