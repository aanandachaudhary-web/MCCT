list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 50, 70, 80, 90]

common = []
only_list1 = []
only_list2 = []

for value in list1:
    if value in list2:
        common.append(value)
    else:
        only_list1.append(value)

for value in list2:
    if value not in list1:
        only_list2.append(value)

print("Common elements:", common)
print("Elements only in list1:", only_list1)
print("Elements only in list2:", only_list2)