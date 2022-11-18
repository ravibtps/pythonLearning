# # Returns False as x is None
# x = None
# print(bool(x))
#
# # Returns False as x is an empty sequence
# x = ()
# print(bool(x))
#
# # Returns False as x is an empty mapping
# x = {}
# print(bool(x))
# # Returns False as x is 0
# x = 0.0
# print(bool(x))


# # Returns True as x is a non empty string
# x = 'GeeksforGeeks'
# print(bool(x))

name=input("Enter the Name : ")
if name=="Ravi":  #True / False
    print(bool(name))
    print("I am in Mumbai")
elif name=="Laddu":
    print(bool(name))
    print("I am in Delhi")
else:
    print("I am in Jaipur")




