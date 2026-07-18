name = input("Enter your name: ")
age = int(input("Enter your age: "))
# f is used so we can add the variable inside {} directly 
print(f"hello {name}!")
print(f"you are {age} years old.")

# some other syntax 

# Modern (recommended)
print(f"Hello {name}!")

# Using +
print("Hello " + name + "!")

# Using .format()
print("Hello {}!".format(name))