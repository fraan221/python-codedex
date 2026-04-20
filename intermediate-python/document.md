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

For Union and Intersection we can use the following:

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

## Functional Programming

### Write code that is easier to understand, test, and maintain with functional programming.

---

## Testing

### Learn how to write basic unit tests in Python.
