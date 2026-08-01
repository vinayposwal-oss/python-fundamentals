# Day 6 - Python Lists

## What is a List?

A list stores multiple values in a single variable.

```python
fruits = ["Apple", "Banana", "Mango"]
```

---

## Indexing

Python starts indexing from **0**.

```python
fruits[0]   # Apple
fruits[1]   # Banana
fruits[-1]  # Mango
```

---

## Slicing

Syntax:

```python
list[start:stop]
```

Examples:

```python
fruits[1:3]
fruits[:2]
fruits[2:]
fruits[::-1]
```

---

## Common List Methods

```python
append()   # Add item to end
insert()   # Add item at index
remove()   # Remove by value
pop()      # Remove by index
sort()     # Sort list
reverse()  # Reverse list
```

---

## Looping Through a List

```python
for item in fruits:
    print(item)
```

---

## Useful Functions

```python
len(list)   # Number of items
max(list)   # Largest value
min(list)   # Smallest value
sum(list)   # Sum of values
```

---

## Key Points

- Lists use `[]`.
- Lists are mutable (can be changed).
- Index starts from `0`.
- `-1` gives the last element.
- Slicing returns a part of the list.
- `for` loop is the easiest way to traverse a list.

---

## Reflection

Today I learned how to create, access, modify, and loop through lists. I also learned common list methods like `append()`, `remove()`, `pop()`, `sort()`, and `reverse()`.