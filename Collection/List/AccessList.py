myList = ["Delhi","Mumbai",'Jaipur']
print(myList[0])
print(myList[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

fruits = ["apple", "banana", "cherry",'mango']

if "mango" in fruits:
  print("Yes, 'this' is in the fruits list")
else:
    print("Not in list")

mylist = ["apple", "banana", "cherry"]
mylist[1] = "Laddu"
print(mylist)

rangeList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
rangeList[1:3] = ["Laddu", "watermelon"]
print(rangeList)

newlist = ["apple", "banana", "cherry"]
print("Old Length :" + str(len(newlist)))
newlist[1:2] = ["Laddu", "watermelon"]
print(newlist)
print("new Length :" + str(len(newlist)))

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)




