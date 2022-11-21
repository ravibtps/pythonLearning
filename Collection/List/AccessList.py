#Creat List
#List items are ordered, changeable, and allow duplicate values.
myList = ["Delhi", "Mumbai", 'Jaipur']
print(myList[0])
print(myList[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

Fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(Fruitlist[2:5])

fruits = ["apple", "banana", "cherry", 'mango']
if "mango" in fruits:
    print("Yes, 'this' is in the fruits list")
else:
    print("Not in list")

mylist = ["apple", "banana", "cherry"]
mylist[1] = "Dragonrfruit"
print(mylist)

rangeList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
rangeList[1:3] = ["Coconut", "watermelon"]
print(rangeList)

newlist = ["apple", "banana", "cherry"]
print("Old Length :" + str(len(newlist)))
newlist[1:2] = ["Grapefruit", "watermelon"]
print(newlist)
print("new Length :" + str(len(newlist)))

Fruitlist = ["apple", "banana", "cherry"]
Fruitlist[1:3] = ["watermelon"]
print(Fruitlist)

#Insert Items
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
