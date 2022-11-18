# fruits = ["apple", "banana", "cherry"]
# fruits.insert(2, "watermelon")
# fruits.insert(0, "coconuts")
# print(fruits)
#
# fruits.insert(3,"Mango")
# print(fruits)

#
# myListcity = ["Delhi","Mumbai",'Jaipur']
# myListcity.append("Goa")
# print(myListcity)

firstlist = ["apple", "banana", "cherry"]
secoundlist = ["mango", "pineapple", "papaya"]
secoundlist.extend(firstlist)
print(firstlist)
print(secoundlist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[1]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print("List cleared "+ str(len(thislist)))
