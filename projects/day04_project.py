# student report card 
name = input("Enter your name ")
sub = int(input("enter number of subject: "))
total = 0

for marks in range(1,sub):
    marks = int(input(f"Enter marks of your{marks} subject: "))
    total += marks

average = total/sub
percentage = (total/(sub*100))*100

if percentage >= 90:
    grade = "A"
elif percentage <=89 and percentage >=75:
    grade = "B"
elif percentage <=74 and percentage >=40:
    grade = "C"
else:
    grade = "Failed"

print("="*20,"Student's Report Card","="*20)
print(f"Name = {name}")
print(f"Subject = {sub}")
print(f"Total = {total}")
print(f"Average = {average}")
print(f"Percentage = {percentage}%")
print(f"Grade = {grade}")
print("="*50)


