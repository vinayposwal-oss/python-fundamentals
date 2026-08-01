print("="*10,"Student Grade Book","="*50)
name = input("Enter Student Name:")
print("Enter Marks For 5 Subject")

total = 0

marks = []
for mark in range(1,6):
    mark = float(input(f"Marks for Subject {mark}:"))
    marks.append(mark)
    total += mark

average = total/len(marks)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
elif average >= 50:
    grade = "E"
else:
    grade = "F"
    print("Fail")

print()
print("Marks:",marks)
print("\n \n")
print("="*20,"Student Report Card","="*20)
print(f"Name = {name}")
print(f"Total Marks = {total}")
print(f"Average Marks = {average}")
print("Highest Marks = ",max(marks))
print("Lowest Marks = ",min(marks))
print(f"Grade = {grade}")
print("="*70)