# Make two lists of any size and then add elements in then make a new list
# with numbers that are present in both lists

list1 = []
list2 = []
common_list = []

# get the number of elements for list1
list1_number = int(input("How many elements are in list1?: "))

# input the numbers into list1
for i in range(0, list1_number):
    element = int(input())
    list1.append(element)

# get the number of elements for list2
list2_number = int(input("How many elements are in list2?: "))

# input for numbers into list2
for i in range(0, list2_number):
    element2 = int(input())
    list2.append(element2)

for l1 in list1:
    if l1 in list2:
        common_list.append(l1)

print(common_list)