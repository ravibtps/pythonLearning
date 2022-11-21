#A tuple is a collection which is ordered and unchangeable.
#Tuple items are ordered, unchangeable, and allow duplicate values.
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
print(thistuple)

#To create a tuple with only one item, you have to add a comma after the item,
# otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)