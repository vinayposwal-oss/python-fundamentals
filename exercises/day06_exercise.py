marks = []
total = 0

def get_average(marks):
    average = total / len(marks)
    return average



print("\n")
print("Enter Marks for 5 subjects")
print("\n")

for mark in range(1,6):
    mark = int(input(f"Subject {mark}: "))
    marks.append(mark)
    total += mark

print("\n")
print("Total Marks =",total)
print("\n")
print("Average Marks:",get_average(marks))
print("\n")
print("Maximum Marks:",max(marks))
print("\n")
print("Minimum Marks:",min(marks))
print("\n")
print("Sorted Marks:",marks.sort())
print("\n")
print("Reversed List of Marks:",marks[::-1])

