# Python Numbers:
# There are three numeric types in Python:
    # int
    # float
    # complex

x = 1
y = 35656222554887711
z = -3255522
print (type(x))
print (type(y))
print (type(z))

x1 = 1.10
y1 = 1.0
z1 = -35.59
x2 = 35e3
y2 = 12E4
z2 = -87.7e100
print (type(x1))
print (type(y1))
print (type(z1))
print (type(x2))
print (type(y2))
print (type(z2))

x3 = 3+5j
y3 = 5j
z3 = -5j
print (type(x3))
print (type(y3))
print (type(z3))

# Note: You cannot convert complex numbers into another number type.

# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
import random
# randint(a, b) → Think: "Give me any integer from a to b, including both."
print(random.randint(1,100)) # This line is commented out, but it would print a random integer from 1 to 100.
# randrange(start, stop, step) → Works like range(), but picks one random value from that range.
print(random.randrange(1,100,5))  # This line is commented out, but it would print a random number from the range 1 to 100 with a step of 5.