# Codédex - Intermediate Python

## Data Structures

### Store data in tuples, dictionaries, and sets.

**Data structures** are containers that lets us organize and store data effectively.

Python list are data structures.

#### Tuples

**Tuples** are ordered collections that cannot be changed after creation.

This means that they are **immutable**, which means their values cannot change. They’re great for data that should stay the same, like coordinates or color values.

Creating a Tuple

```
person = ('Kat', 24)
navy_blue = (0, 0, 128)
```

Tuples are created using `(` `)` parentheses.

They are also defined without parentheses and their items can be a mix of any data type. They can have one or more items.

```
# valid tuple
t1 = ('hi',)

# valid tuple
t2 = 'hi',

# not a tuple
t3 = ('hi')
```

If there is only one item, make sure there is a comma `,` beside it.

##### Using Tuples

Tuples are also unpackable which allows us to easily turn them into variables. Most commonly, tuples are used as return values allowing us to easily work with large data sets.

```
full_name = ('Ada', 'Lovelace')

first_name = full_name[0]

print(first_name) # Output: Ada
```

Combining Tuples

```
# Combining tuples
t1 = 'a',
t2 = 'b',
t3 = t1 + t2

print(t3)  # Output: ('a', 'b')
```

#### Dictionaries

Dictionaries are ordered collections that store and access data using `key`:`value` pairs.

Syntax

```
dictionary = {
  key1: value1,
  key2: value2,
  key3: value3
}
```

Example

```
laptop = {
  'brand': 'Apple',
  'model': 'Macbook Pro',
  'size': 14,
  'year': 2023
}
```

Accesing the info in the Dictionary

```
print(laptop['model']) # Output: Macbook Pro
```

Modifying dictionary elements

```
laptop['year'] = 2026
print('Updated year:', laptop['year'])
```

##### Dictionary Methods

- `.keys()` returns just the keys from a dictionary.
- `.values()` returns just the values.
- `.items()` returns a list of the key-value pairs as tuples.

Example

```
print('Keys:', laptop.keys())
print('Values:', laptop.values())
print('Items:', laptop.items())
```

Output

```
Keys: dict_keys(['brand', 'model', 'size', 'year'])
Values: dict_values(['Apple', 'Macbook Pro', 14, 2023])
Items: dict_items([('brand', 'Apple'), ('model', 'Macbook Pro'), ('size', 14), ('year' 2023)])
```

#### Sets

Sets are collections of unique items with no duplicates.

- They are an unordered collection of distinct elements.
- Each item in a set must be unique.

Sets do not have an inherent order.

##### Creating Sets

Syntax

```
set_example = {val1, val2, val3}
```

Example

```
fruits = {'🍎 apple', '🍌 banana', '🍊 orange'}
```

**Note:** Dictionaries and sets can be made with curly braces but set do not use key-value pairs.

##### Using Sets

Sets to combine sets, find common items, or filtering out items

- `.union()`: Combines two or more sets and returns a new set.
- `.intersection()`: Returns a set of items common to two or more sets.
- `.difference()`: Returns a set of items found only in the calling set.

Example

```
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union of sets
union_result = set1.union(set2)

# Intersection of sets
intersection_result = set1.intersection(set2)

# Difference of sets
difference_result = set1.difference(set2)

print(union_result)
print(intersection_result)
print(difference_result)

# Output:
# {1, 2, 3, 4, 5, 6}
# {3, 4}
# {1, 2}
```

Example 1.0

```
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union of sets
union_result = set1 | set2

# Intersection of sets
intersection_result = set1 & set2

# Difference of sets
difference_result = set1 - set2

print(union_result)
print(intersection_result)
print(difference_result)

# Output:
# {1, 2, 3, 4, 5, 6}
# {3, 4}
# {1, 2}
```

Methods for common operations

```
my_set = {1, 2, 3}

my_set.add(4)
print(my_set) # Output: {1, 2, 3, 4}

my_set.remove(2)
print(my_set) # Output: {1, 3, 4}
```

- `.add()` method adds one new item to a set. If that item already exists, nothing happens.
- `.remove()` method removes an item from a set if it exists.

---

## File I/O

### Save and read to a file using file input & output.

---

#### File Handling

File I/O (Input/Output) Handling let us interact with external files for various purposes, including:

- Saving information to a file by writing to it.
- Reading from a file to use its information.
- Maintaining your computer's file system.

##### Opening Files

```
file = open(file_path, mode)
```

This function returns an object that we can save to a variable like file.

The `open()` function takes two arguments:

- The `file_path`, such as `'filename.txt'`.
- The `mode` for how to use the file.

There are three modes you can open a file with:

- `'r'` for reading a file. 📖
- `'w'` for writing to a file. ✍🏼
- `'a'` for writing from the end of a file. 📝

**Note:** Be careful with `'w'` mode. It will overwrite any existing file content. Use `'a'` to avoid this.

##### Writing Files

```
file.write('text')
```

A string is passed to the `write()` method, and written to the file.

You can also write multiple lines to a file at once with the `writelines()` method:

```
lines = ['This is a line.\n', 'This is the next line.\n']

file.writelines(lines)
```

The `writelines()` method takes a list of lines and writes them to the file.

##### Reading Files

The `read()` method lets you read the entire content of a file.
This method can be saved to a variable and printed to the terminal:

```
file = open('filename.txt', 'r')

content = file.read()

print('Using read():')
print(content)
```

The `.readline()` method lets you read a file one line at a time:

```
line1 = file.readline()  # Read the first line
print(line1, end='')     # Printing the first line

line2 = file.readline()  # Read the second line
print(line2, end='')     # Printing the second line
```

To print each line on a single line without adding a `'\n'` newline character at the end, we use the `end=''` option in the `print()` function.

**Note:** By default, `print()` ends with a `'\n'` newline character.

The `.readlines()` method lets you read all lines in a list:

```
lines = file.readlines()

for line in lines:
  print(line, end='')
```

##### Closing Files

To open a file, handle it, and close it automatically:

```
with open('filename', 'r') as f:
  # handle file here
```

Note: This is the Best Practice for Handling Files in Python.

##### Safe File Handling

To prevent a file from remaining open if an error occurs, there are two main approaches to ensure it closes properly:

- `try-finally` block: This is the manual approach. The code inside the finally block executes no matter what happens (even if an exception is raised).

```
try:
    file = open('example.txt', 'r')
finally:
    file.close() # Guaranteed closure
```

- `with` statement (Recommended): This acts as a Context Manager that automatically closes the file when the block ends, without the need to explicitly call .close().

```
with open('example.txt', 'r') as file:
content = file.read()
```

##### The File Cursor

It is the position indicator (like a blinking text pointer) inside the file.

- `.seek(n)`: Moves the cursor to byte (position) **n**.

- `.read()`: Reads the file content starting from the current cursor position until the end of the file.

##### File Size Manipulation

- `.truncate(n)`: Resizes the file to exactly **n** bytes.
  - If the file is larger than **n**, the extra content is deleted (trimmed).
  - If the file is smaller, it extends the file (usually padding it with null bytes).

###### Modes with `open()` function

- `r+` is used to indicate both reading and writing are allowed in the file.

#### CSV Files

A **CSV(Comma-Separated Values)** file is a standard format for organizing tabular data. Each row represents a record, and the values within are separated by commas. Python handles these seamlessly with the built-in csv module.

##### Reading CSV Files

To read a CSV file, use the `csv.reader()` method. It reads the file and returns an iterable object where each row is converted into a list of strings.

- **Crucial Tip:** Always include encoding='utf8' when opening the file to prevent decoding errors (very common depending on the IDE or OS you are using).

```
import csv

# Open the file in 'read' mode ('r') with UTF-8 encoding
with open('example.csv', 'r', encoding='utf8') as file:
    csv_reader = csv.reader(file)

    # Iterate through the reader object row by row
    for row in csv_reader:
        print(row)  # Output: A list representing the row's data
```

##### Writing to CSV Files

To write data—typically structured as a list of lists—into a CSV, use the `csv.writer()` method.

- Crucial Tip: Always include newline='' when opening the file in write mode. This prevents Python from accidentally adding extra blank lines between your rows.

- `.writerows()`: A writer method that takes an iterable (like a list of lists) and writes multiple rows at once.

```
import csv

# Data structured as a list of lists
data_to_write = [
['Name', 'Age', 'Grade'],
['Alice', 25, 'A'],
['Bob', 22, 'B'],
['Charlie', 28, 'A+']
]

# Open the file in 'write' mode ('w') with newline=''
with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)

    # Write the entire data block to the CSV file
    csv_writer.writerows(data_to_write)
```

---

## Functional Programming

### Write code that is easier to understand, test, and maintain with functional programming.

#### Pure Function

Functional Programming is a coding paradigm that approaches problem-solving by structuring code primarily around functions.

Pure Functions
A pure function is the core building block of this paradigm. It is defined by two main rules:

1. **Output depends solely on inputs:** It does not rely on, reference, or modify external/global variables.
2. **No side effects:** It does not interact with the outside world (e.g., no printing to the console, no writing to files, no modifying data outside its scope).

Because of these rules, pure functions are highly predictable, reliable, and easy to test. They will always return the exact same result if given the exact same input.

**Code Comparison: Pure vs. Impure**

```
# ❌ Impure Function
# It has a "side effect" because it prints something to the terminal.
def impure_squared(number):
    result = number ** 2
    print('The square of', number, 'is', result)  # This is the side effect!
    return result

# ✅ Pure Function
# It strictly takes an input, calculates, and returns the output. No side effects.
def pure_squared(number):
    return number ** 2
```

#### Higher Order Functions

In functional programming, higher-order functions can take other functions as arguments or return functions as results.

##### Example

```
# Define the Higher-order function
def apply_operation(operation, numbers):
  result = []
  for num in numbers:
    result.append(operation(num))
  return result

# Example operation
def double(x):
  return x * 2

# List of numbers
numbers_list = [1, 2, 3, 4, 5]

# Using the higher-order function
doubled_numbers = apply_operation(double, numbers_list)

# Displaying the outcomes
print('Original Numbers:', numbers_list)
print('Doubled Numbers:', doubled_numbers)
```

##### Result

```
Original Numbers: [1, 2, 3, 4, 5]
Doubled Numbers: [2, 4, 6, 8, 10]
```

#### Transform Data

In Python, we can transform data using three powerful functions: `map()`, `filter()`, and `reduce()`. These functions allow us to **manipulate**, **select**, and **aggregate** data efficiently.

##### map() Function

Syntax:

```
map(function, data)
```

`map()` applies the given `function` to each element in the `data` and returns a new list. It's perfect for when you need to perform the same operation on every item in a list, tuple, or data set.

Example

```
def divide_by_2(x):
  return x / 2

halved_numbers = map(divide_by_2, [1, 2, 3, 4, 5])

print(list(halved_numbers))
# Output: [0.5, 1.0, 1.5, 2.0, 2.5]
```

**Note:** To get the actual list, we need to use the `list()` function.

##### filter() Function

Syntax

```
filter(function, data)
```

Here, we select elements from the `data` that satisfy the given condition specified by the `function` and return a new list. It helps extract specific items from a dataset based on the criteria you define. The input function in `filter()` must return a boolean.

Example

```
def filter_even(x):
  return x % 2 == 0

even_numbers = filter(filter_even, [1, 2, 3, 4, 5])

print(list(even_numbers)) # Output: [2, 4]
```

##### reduce() Function

Syntax

```
from functools import reduce
reduce(function, data, initial)
```

`reduce()` takes a collection of iterable `data` and combines its elements into a single value via a `function`. An optional `initial` value can be used, as well.

This function is ideal for tasks like summing up a list of numbers.

Example

```
from functools import reduce

def multiply(x, y):
  return x * y

product = reduce(multiply, [1, 2, 3, 4, 5])

print(product) # Output: 120
```

#### List Comprehensions

**List comprehensions** can transform _data_, _filter elements_, and even _create nested lists_. In functional programming, they let us transform list data concisely and expressively.

Syntax

```
[expression for item in dataset if condition]
```

1. The `expression` is applied to each `item`.
2. A `for..in` statement loops through each `item`.
3. An optional `if condition` can filter out items.

The `dataset` can be something iterable like a list or tuple.
List comprehensions do not change the original list.

**Note:** A list comprehension works with `for` loops but not `while` loops.

Example

```
# Original approach using a loop
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
  squares.append(num ** 2)

# Using a list comprehension to square each number
squared_numbers = [num ** 2 for num in numbers]

# Displaying the outcomes
print('Original Numbers:', numbers)
print('Squared Numbers:', squared_numbers)
```

#### Decorators

Functions that modify, extend, or wrap the behavior of another function dynamically, without altering its original source code.

Syntax & Example:
It uses the @decorator_name syntax placed directly above the target function.

```
# 1. Define the decorator (the wrapper)

def my_decorator(func):
def wrapper():
print('Before function execution')
func() # The original function executes here
print('After function execution')
return wrapper

# 2. Apply the decorator using @

@my_decorator
def say_hello():
print('Hello, decorators!')

# 3. Call the decorated function

say_hello()
```

#### Generators

Special functions that generate a sequence of values dynamically. Instead of storing all values in memory and returning them at once, they pause execution and produce one value at a time, making them highly memory-efficient for iterating over large datasets.

Syntax & Example:
Defined like a normal function, but uses the yield keyword instead of return.

```
# 1. Define the generator function using yield
def square_generator(limit):
    num = 1
    while num <= limit:
        yield num ** 2  # Pauses execution and returns this value
        num += 1

# 2. Iterate over the generated values
for square in square_generator(5):
    print(square)  # Outputs step by step: 1, 4, 9, 16, 25
```

---

## Testing

### Learn how to write basic unit tests in Python.
