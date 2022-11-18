thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
print()

# **********************************************************************#
# Loop Through the Index Numbers
carlist = ["Audi", "BMW", "Ferrari"]
for i in range(len(carlist)):
    print(carlist[i])
print()

# **********************************************************************#
# While Loop
citylist = ["Copenhagen", "Oslo", "Bergen"]
i = 0
while i < len(citylist):
    print(citylist[i])
    i = i + 1
print()
# **********************************************************************#
# List Comprehension  A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

