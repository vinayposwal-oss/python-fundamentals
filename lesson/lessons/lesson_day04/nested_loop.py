# nesteed loops 
for i in range(5):
    for j in range(5):
        print("*", end=" ") # end=" " is used to print space in the same line
    print("") #move to the next line

# Table of 1 to 3
for row in range(1,4):
    for col in range(1,11):
        print(row*col,end="  ")# end=" " is used to print space in the same line
    print("") #move to the next line
    