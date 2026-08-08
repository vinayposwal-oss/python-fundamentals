# Day 7 - Tuples & Dictionaries

## 1. Tuples

A tuple is a collection of values that cannot be changed after it is created.

```python
months = ("Jan", "Feb", "Mar")
```

### Features

- Uses `()`
- Ordered
- Allows duplicate values
- Supports indexing and slicing
- Immutable → cannot be changed

### Accessing Elements

```python
months[0]    # Jan
months[-1]   # Mar
```

### Length

```python
len(months)
```

---

## 2. List vs Tuple

Use a **list** when data may change.

```python
marks = [80, 90, 75]

marks[0] = 85
```

Use a **tuple** when data should remain fixed.

```python
days = ("Monday", "Tuesday", "Wednesday")
```

Trying to change a tuple:

```python
days[0] = "Sunday"
```

will cause an error.

### Remember

```text
List  → changing data
Tuple → fixed data
```

Examples:

```python
shopping = ["Milk", "Bread"]       # List
months = ("Jan", "Feb", "Mar")     # Tuple
```

---

# 3. Dictionaries

A dictionary stores data using **key-value pairs**.

```python
student = {
    "name": "Vinay",
    "age": 20,
    "course": "AI Engineering"
}
```

Here:

```text
"name"   → key
"Vinay"  → value

"age"    → key
20       → value
```

Unlike lists, dictionaries use **keys instead of indexes**.

---

## 4. Accessing Dictionary Values

Use the key:

```python
print(student["name"])
```

Output:

```text
Vinay
```

Another example:

```python
print(student["course"])
```

Output:

```text
AI Engineering
```

---

## 5. Adding Data

A new key can be added by assigning a value.

```python
student["status"] = "Active"
```

---

## 6. Updating Data

Use an existing key to change its value.

```python
student["age"] = 21
```

The old value `20` is replaced with `21`.

---

## 7. Removing Data

`pop()` removes an item using its key.

```python
student.pop("age")
```

---

## 8. Useful Dictionary Methods

### keys()

Returns all keys.

```python
student.keys()
```

### values()

Returns all values.

```python
student.values()
```

### items()

Returns key-value pairs.

```python
student.items()
```

---

## 9. Looping Through a Dictionary

Use `items()` to get both the key and value.

```python
for key, value in student.items():
    print(key, value)
```

Example output:

```text
name Vinay
age 21
course AI Engineering
```

---

## 10. Dictionary with a List

A dictionary can contain a list as a value.

```python
student = {
    "name": "Vinay",
    "marks": [85, 90, 78]
}
```

Access the list:

```python
print(student["marks"])
```

Access an individual mark:

```python
print(student["marks"][0])
```

Output:

```text
85
```

This combination is very common when working with structured data.

---

# List vs Tuple vs Dictionary

| Data Structure | Best For | Can Change? |
|---|---|---|
| List | Changing collections | Yes |
| Tuple | Fixed collections | No |
| Dictionary | Key-value data | Yes |

### Easy Reminder

```text
List       → [values]
Tuple      → (fixed values)
Dictionary → {key: value}
```

---

# Key Takeaways

- Tuples are ordered and immutable.
- Lists are mutable.
- Dictionaries store key-value pairs.
- Dictionaries use keys instead of indexes.
- `student["name"]` accesses a value.
- `student["key"] = value` adds or updates data.
- `pop()` removes a dictionary item.
- `keys()` returns keys.
- `values()` returns values.
- `items()` returns key-value pairs.
- `items()` is useful when looping through dictionaries.

## Reflection

Today I learned about tuples and dictionaries. I learned when to use a list, tuple, or dictionary and how to create, access, update, add, remove, and loop through dictionary data.