# Write a Python program that collects information about a student and displays it in a well-formatted profile while also showing the data type of each input.
print("="*50)
print("Student AI Engineering Profile")
print("="*50)

# input 
name = input("Enter your  Full name: ")
age = float(input("Enter your age: "))
city = input("Enter your city: ")
clg = input("Enter your college: ")
fav = input("Enter your favorite programming language: ")
ai_intrest = input("Enter your favorite ai interest field: ")

#display portfolio 
print("-"*5,"Student Profile", "-"*5)
print(f"Full Name            : {name}")
print(f"Age.                 : {age}")
print(f"City                 : {city}")
print(f"College              : {clg}")
print(f"Favorite Programming : {fav}")
print(f"Favorite AI Intrest  : {ai_intrest}")
#Types of variable 
print("-"*5,"Data Types", "-"*5)
print(f"Full name              :{type(name)}")
print(f"Age                    :{type(age)}")
print(f"City                   :{type(city)}")
print(f"College                :{type(clg)}")
print(f"Favorite Programming   :{type(fav)}")
print(f"Favorite AI Intrest    :{type(ai_intrest)}")

print(f"-"*5,"End of Profile and Day 02 Exercise", "-"*5)