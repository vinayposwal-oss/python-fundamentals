student = {
    "Name":"Vinay Poswal",
    "Age":20,
    "Course":"CSE AI and ML",
    "Marks":[20,43,65,29]

}

print("Student Name :",student["Name"])
print("Student Course :",student["Course"])
average = sum(student["Marks"])/len(student["Marks"])
print(average)
student["Status"] = "active"
student["Age"] = 22

for key ,value in student.items():
    print(key,":",value)
