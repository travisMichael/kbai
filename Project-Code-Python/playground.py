myList = []
myList.append('Goodbye')
myList.append('Hello')

print(myList.pop())
print(myList.pop())

list1 = [1, 2, 3]

list2 = list1[:]
list3 = list1[:]

list2.append(4)

print(list3)
print("--------")
print(list2)