#Remove
#Tuples are unchangeable
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
print()

#del keyword
thistuple = ("apple", "banana", "cherry")
del thistuple
try:
    print(thistuple)  # this will raise an error because the tuple no longer exists
except:
    print("thistuple is deleted")

