# create empty list
my_list = []

# appended some element to an empty list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert value 15 in the second postion which is 1
my_list.insert(1, 15)

# another list
another_list = [50, 60, 70]
# extendend my list with another list called another list.
my_list.extend(another_list)

# remove last element in the list
my_list.pop(-1)

# order my list in ascending order
my_list.sort()

# index of 30 and print the value of its index
index_of_30 = my_list.index(30)
print("The index of 30 is:", index_of_30)
