# Write a program called Student Eligibility Checker.
name = input("Enter your Full name: ")
age = int(input("Enter your Age: "))
marks = int(input("Enter your Marks out of 100: "))

# check eligiblity and marks to pass the exam

if age >=18 :
    print("voting status : Eligible")
    if marks >= 40:
        print("Result : Passed the exam")
    else:
        print("Result : Failed the exam")
elif age < 18 and marks >= 40:
    print("voting status : Not Eligible\nResult : Passed the exam")
else:
    print("voting status : Not Eligible\nResult : Failed the exam")

# cheking grade based on marks

if marks >= 90:
    print("grade : A")
elif marks >= 75 and marks <=89:
    print("grade : B")
elif marks >= 40 and marks <= 74:
    print("grade : C")
else:
    print("failed the exam")

