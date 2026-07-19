 # Day 4 - Loops

## What is a Loop?

A loop is used to repeat a block of code multiple times without writing the same code again and again.

Example:

Instead of writing:

```python
print("Hello")
print("Hello")
print("Hello")
```

We can write:

```python
for i in range(3):
    print("Hello")
```

The output is the same, but the code is much cleaner.

---

# Types of Loops

Python has two types of loops:

1. for loop
2. while loop

---

# 1. for Loop

A `for` loop is used when we already know how many times we want to repeat something.

### Syntax

```python
for variable in range(start, stop, step):
    # code
```

Example:

```python
for i in range(1, 6):
    print(i)
```

Output:

```
1
2
3
4
5
```

### Understanding `range()`

`range()` generates a sequence of numbers.

Examples:

```python
range(5)
```

Output:

```
0 1 2 3 4
```

```python
range(1, 6)
```

Output:

```
1 2 3 4 5
```

```python
range(2, 11, 2)
```

Output:

```
2 4 6 8 10
```

> **Remember:** The stop value is **not included**.

---

# 2. while Loop

A `while` loop runs as long as a condition is `True`.

### Syntax

```python
while condition:
    # code
```

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```
1
2
3
4
5
```

### Important

Always update the variable inside a `while` loop.

Otherwise, the loop may never stop (called an **infinite loop**).

Example:

```python
while True:
    print("Hello")
```

This will keep printing forever.

---

# Difference Between `for` and `while`

| for Loop | while Loop |
|----------|------------|
| Used when the number of iterations is known | Used when the number of iterations is unknown |
| Uses `range()` or a sequence | Uses a condition |
| Example: Print numbers 1–10 | Example: Keep asking for a password |

---

# Nested Loops

A nested loop is a loop inside another loop.

Example:

```python
for row in range(3):
    for col in range(4):
        print("*", end=" ")
    print()
```

Output:

```
* * * *
* * * *
* * * *
```

### Remember

- Outer loop → Rows
- Inner loop → Columns

---

# Common Mistakes

- Forgetting the `:` after the loop.
- Incorrect indentation.
- Forgetting to update variables in a `while` loop.
- Thinking `range(1,5)` includes 5 (it doesn't).

---

# Key Takeaways

- Loops help automate repetitive tasks.
- Use a `for` loop when the number of repetitions is known.
- Use a `while` loop when repetition depends on a condition.
- Nested loops are useful for working with rows and columns.

---

# Reflection

Today I learned how to use `for` loops, `while` loops, and nested loops to write cleaner and more efficient programs. I also understood when to use each type of loop and the importance of updating conditions in a `while` loop.