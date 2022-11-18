CustomizeSort = ["orange", "mango", "kiwi", "pineapple", "banana"]
CustomizeSort.sort()
print(CustomizeSort)
print()
# *****************************************************************************#
CustomizeSort = ["orange", "mango", "kiwi", "pineapple", "banana"]
CustomizeSort.sort(reverse=True)
print(CustomizeSort)
print()
# *****************************************************************************#
def sortfunc(n):
    return abs(n - 50)


CustomizeSort = [100, 50, 65, 82, 23]
CustomizeSort.sort(key=sortfunc)
print(CustomizeSort)
print()
# *****************************************************************************#
# case-insensitive sort
case_insensitive_sort = ["banana", "Orange", "Kiwi", "cherry"]
case_insensitive_sort.sort(key=str.lower)
print(case_insensitive_sort)
print()
# *****************************************************************************#
# Reverse Order
reverse_order = ["banana", "Orange", "Kiwi", "cherry"]
reverse_order.reverse()
print(reverse_order)