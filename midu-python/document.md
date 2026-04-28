# Midudev - Python

## Type Hints

Python is a dynamically typed language, which means a variable's type is determined at runtime and can change. Type annotations are basically a way to document your code, indicating what type you expect a variable to have.

The key point, and something that is surprising at first, is that Python completely ignores these annotations at runtime. If you declare a variable as `bool` and assign a number to it, the program still runs without breaking:

```python
is_user_locked: bool = True
is_user_locked = 42  # Python doesn't complain, it executes it anyway
```

For annotations to be truly useful, you need to enable strict Type Checking in your editor. In VS Code, you can set it to strict mode, and from then on, it's the editor that warns you with a red underline if you assign an incorrect type. It's not Python doing the validation, it's your development environment.

## Operador Ternario

It's a way to write an if/else statement in a single line. Python's syntax is particular because the value returned if the condition is true goes first, before the `if`:

```python
age = 17
message = "Is of legal age" if age >= 18 else "Is underage"
print(message)  # "Is underage"
```

The structure is always: `value_if_true if condition else value_if_false`. At first, it feels backwards compared to other languages, but after a couple of uses, it becomes quite natural to read.

## Iteration with `enumerate()`

`enumerate()` is for when you need both the index and the value at the same time in a loop. Instead of messing around with manual counters, you wrap it in the `for` and it gives you both:

```python
fruits = ["apple", "pear", "tangerine"]
for idx, value in enumerate(fruits):
    print(f"The index is {idx} and the fruit is {value}")
```

## Function Arguments

### Three variants

- Named: you pass arguments using the parameter name, so order doesn't matter:

```python
describe_person(sex="cat", name="midudev", age=25)
describe_person(sex="male", name="madeval", age=21)
```

- `*args`: for when you don't know how many arguments are coming in. Groups them into a tuple and you iterate with a `for`:

```python
def sum_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total

print(sum_numbers(1, 2, 3, 4, 5))
print(sum_numbers(1, 2))
print(sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
```

- `**kwargs`: same but with named arguments. Groups them into a dictionary, you can pass whatever you want:

```python
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="midudev", age=25, sex="cat")
show_info(name="madeval", age=21, country="Uruguay")
show_info(super_name="felixicaza", is_mod=True, cats=40)
```

## Regex

**Regular Expressions (Regex)** — the module that lets you search, validate and manipulate text using patterns. Just import `re`, no install needed.

### Importing and searching (`re.search`)

Always write patterns with `r"..."` (raw strings) so Python doesn't misread escape characters:

```python
import re

text = "Hello world"
pattern = "Hello"
result = re.search(pattern, text)

if result:
    print(result.group())   # Returns the match: "Hello"
    print(result.start())   # Start index
    print(result.end())     # End index
```

### Multiple search and replace

**`findall()`** returns a list with every match:

```python
text = "I love Python. Python is great. Python is not that hard either"
matches = re.findall("Python", text)
print(len(matches))  # 3
```

**`finditer()`** does the same but lets you get `.start()` and `.end()` for each match:

```python
for match in re.finditer("Python", text):
    print(match.group(), match.start(), match.end())
```

**`sub()`** works as a find and replace:

```python
new_text = re.sub("hello", "goodbye", "Hello, world! Hello again.", flags=re.IGNORECASE)
```

**`re.IGNORECASE`** ignores uppercase/lowercase differences:

```python
found = re.findall("AI", text, re.IGNORECASE)
```

### Metacharacters

`.` matches any character except newline, so `H.llo` matches `Hello`, `H3llo`, `H$llo`. `\d` matches any digit, useful for phone number detection:

```python
pattern = r"\+1 \d{10}"
found = re.search(pattern, "My number is +1 6889999999")
```

`\w` matches any alphanumeric character plus underscore, `\s` matches any whitespace (space, tab, newline). `^` and `$` anchor the pattern to the start or end of the string:

```python
pattern = r"^\w"        # username must start with alphanumeric
pattern = r"@gmail\.com$"  # validates a gmail address
```

`\b` sets a word boundary to avoid partial matches, `|` works as OR between options, and `\` cancels a metacharacter's special power:

```python
pattern = r"\bh.use\b"   # matches "house" but not "household"
pattern = r"cat|dog"     # matches either "cat" or "dog"
pattern = r"\."          # searches for a literal dot, not the wildcard
```

### Quantifiers and Sets

**Quantifiers** control how many times something appears. `+` means 1 or more, `*` means 0 or more, `?` makes something optional (handy for country codes), and `{n,m}` sets an exact range:

```python
pattern = r"(\+1 )?\d{10}"        # makes the +1 prefix optional
pattern = r"\b\w{4,6}\b"          # words between 4 and 6 letters
matches = re.findall(pattern, "sky house elephant tree piano motorcycle")
```

**Sets `[...]`** let you define your own character rules when `\w` or `\d` aren't specific enough:

```python
pattern = r"[aeiou]"       # any vowel
pattern = r"[mfb]an"       # matches "man", "fan", "ban" but not "ran"
pattern = r"[^aeiou]"      # anything that is NOT a vowel

# Custom set for username validation
pattern = r"^[\w._%+-]+$"
match = re.search(pattern, "john.doe_99+")
```

## Dates

### Current moment and specific dates

- `datetime.now()` gives you the exact current instant.
- To set a date manually just pass the numbers directly: `datetime(2025, 2, 12, 15, 30)`. No weird math, no subtracting 1 from the month — February is 2, period.
- You can pull out specific pieces from any date object: `now.year`, `now.month`, `now.day`, etc.

### Formatting dates (`strftime`)

The raw `datetime` object looks ugly in the console, so you use `strftime` with `%` directives to shape it however you want:

```python
now = datetime.now()
formatted = now.strftime("%d/%m/%Y")
print(formatted)  # 05/03/2026
```

### Time travel with `timedelta`

Add or subtract blocks of time from any date in a really readable way:

```python
from datetime import timedelta

yesterday = datetime.now() - timedelta(days=1)
tomorrow = datetime.now() + timedelta(days=1)
next_week = datetime.now() + timedelta(weeks=1)
```

You can even pass fractions like `timedelta(days=0.5)` to add exactly half a day.

### Difference between two dates

Just subtract two date objects and Python automatically returns a `timedelta` with the exact difference. Then you can ask for `.days` or `.seconds` on it.

### Language trick (`locale`)

By default `strftime` prints day and month names in English. To switch to Spanish, import the native `locale` module and configure it with `locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')`. Worth noting: words like "marzo" or "miércoles" come out lowercase — not a bug, it's following the RAE rule that days, months and seasons in Spanish are written in lowercase.
