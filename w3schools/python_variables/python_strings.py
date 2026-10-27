# Python Strings:
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

print("Hello")
print('Hello')

# Quotes Inside Quotes
print("It's alright.") # You can use double quotes inside a string if the string is surrounded by single quotes.
print('He said "Hello".') # You can use single quotes inside a string if the string is surrounded by double quotes.
print("He said \"Hello\".") # You can use the escape character \ to insert characters that are illegal in a string.

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut
labore et dolore magna aliqua."""
print(a)
