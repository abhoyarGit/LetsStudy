s1 = "This is Day2. We are studying Sting-methods"
s2 = "außen"

# capitalize()	Converts the first character to upper case. Rest all Lower Case.
print(s1.capitalize())  # This is day2. we are studying sting-methods
print(s2.capitalize())  # Außen

#  casefold()   Converts string into lower case
print(s1.casefold())  # this is day2. we are studying sting-methods
print(s2.casefold())  # aussen

#  lower()	Converts a string into lower case
print(s1.lower())     # this is day2. we are studying sting-methods
print(s2.lower())     # außen


s3 = "Hello"
S4 = "Hope"
'''
Center  'Return a centered string of length width.\n\nPadding is done using the specified fill character (default is a space).
'''
print(s3.center(8, "*"))  # *Hello**


#  count()	Returns the number of times a specified value occurs in a string
print(s3.count("l"))  # 2

#  index()	Searches the string for a specified value and returns the position of where it was found
print(s3.index("e"))   # 1
print(s3[2])  # l

#  len   Return length of String
print(len(s3))  # 5

#  find()	Searches the string for a specified value and returns the position of where it was found
s3 = "Hello"
print("Find - ", s3.find("o"))           # 4
print("Find - ", s3.find("H", 0, 1))     # 0
print("Find - ", s3.find("H", 1, 5))     # -1
print("Find - ", s3.find("o", 0, 5))     # 4
print("Find - ", s3.find("h", 0, 5))     # -1
print("Find - ", s3.find("1", 0, 5))     # -1

#  format()	Formats specified values in a string
s3 = "Hello {}"
print(s3.format("Format"))

tuple.__dir__()
