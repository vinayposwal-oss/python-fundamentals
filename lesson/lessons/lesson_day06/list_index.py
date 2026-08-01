# Positive Index
# 0        1        2        3
# Apple   Banana   Mango   Orange
# Negative Index
# -4      -3       -2      -1
marks = [10,43,45,75,83]
print("index 0 =",marks[0]) 
print("index 1 =",marks[1])
print("index 2 =",marks[2])
print()
print("index 0 =",marks[-5]) 
print("index 1 =",marks[-4])
print("index 2 =",marks[-3])
# list[start:stop] syntax
print(marks[1:3])
print(marks[:3]) # python assume starting as 0
print(marks[3:]) # goes till end 
# list[start:stop:step] slicing 
print(marks[::2]) #step = 2,take every second element
print(marks[::-1]) # reverse the whole list
