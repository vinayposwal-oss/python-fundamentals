fruits = ["apple","mango"]
print("before =",fruits)
# The append() method adds one item to the end of the list.
fruits.append("banana")
print("after =",fruits)

#list.insert(index, value)  Add at a Specific Position
fruits.insert(2,"orange")
print("after insert at index 3 =",fruits)

# remove() deletes the first matching value.
fruits.remove("banana")
print(fruits)

# pop() removes an item using its index.
fruits.pop(2)
print("after pop() index 2 =",fruits) # if index not given remove last item pop()

#sort() – Arrange in Order
marks = [10,43,4,29,45,32]
print("before sort() =",marks)
marks.sort()
print("after sort() =",marks) # if sting sort by alphabets

#reverse() – Reverse the List
marks.reverse()
print("after reverse() =",marks)