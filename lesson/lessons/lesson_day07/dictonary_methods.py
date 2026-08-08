student = {
    "Name":"vinay",
    "Age": 22,
    "Course":"python",
    "college":"XYZ University"
}

#updating the name in dictonary of students
print("Before update name =",student["Name"])
student["Name"] = "Viany Poswal"
print("after update name =",student["Name"])

print()

# Removing an item from the dictionary using pop() method
print("Before removing course =",student)
student.pop("Course")
print("After removing course =",student)

print()

#get all key of dictonary using key() method
print("All keys in student dictionary:", student.keys())

print()

#get all values of dictonary using values() method
print("All values in student dictionary:", student.values())

print()

# get all items of dictonary using items() method
print("All items in student dictionary:", student.items())

print()

# loop in dictonary
for key, value in student.items():
    print(key, ":", value)