x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("Mango",)
thistuple += y

print(thistuple)