# Day 5 - Functions

## Lesson 1 - Introduction to Functions

### What is a Function?

A function is a reusable block of code that performs a specific task. It helps reduce repetition and makes programs easier to read, maintain, and debug.

### Syntax

```python
def function_name():
    # code
```

Example:

```python
def greet():
    print("Hello")

greet()
```

### Key Points

- `def` is used to define a function.
- A function does not execute when it is created.
- A function executes only when it is called.
- Functions improve code reusability.

---

## Lesson 2 - Parameters & Arguments

### Parameter

A parameter is a variable defined in a function that receives values.

Example:

```python
def greet(name):
    print(name)
```

`name` is the parameter.

### Argument

An argument is the actual value passed to a function.

Example:

```python
greet("Vinay")
```

`"Vinay"` is the argument.

### Multiple Parameters

```python
def student(name, age):
    print(name, age)

student("Vinay", 20)
```

---

## Lesson 3 - Return Statement

### What is Return?

The `return` statement sends a value back to the place where the function was called.

Example:

```python
def add(a, b):
    return a + b

result = add(5, 10)
print(result)
```

### print() vs return

| print() | return |
|----------|---------|
| Displays output | Sends value back |
| Cannot be reused | Can be stored in variables |
| Mainly for displaying | Mainly for calculations |

### Key Points

- `return` ends the function immediately.
- Returned values can be reused later.

---

## Lesson 4 - Variable Scope

### Local Scope

Variables created inside a function.

```python
def greet():
    name = "Vinay"
```

Accessible only inside the function.

### Global Scope

Variables created outside every function.

```python
name = "Vinay"

def greet():
    print(name)
```

Accessible throughout the program.

### Best Practices

- Prefer local variables.
- Use global variables only when many functions need the same value.

---

## Reflection

Today I learned how to create reusable functions using parameters and arguments. I also understood the difference between `print()` and `return`, and learned how local and global variables affect where data can be accessed.