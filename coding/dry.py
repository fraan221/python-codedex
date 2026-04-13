# This is the first function we've seen in the course.
print("Hello!")

# Return the largest item in an iterable or the largest of two or more arguments.
print(max(200, 500))

# Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).
list = [1, 'abc', True]
print(len(list))

# Return a str version of object.
number = 1231231
print(str(number))

# Convert an integer number to a binary string prefixed with “0b”. The result is a valid Python expression. If integer is not a Python int object, it has to define an __index__() method that returns an integer.
print(bin(3))