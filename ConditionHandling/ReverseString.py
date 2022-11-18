x = input("Please Enter : ")
# x = "My Name is Ravi"
a = ""

length = len(x)
# print(length)

for i in range(length-1, -1, -1):
    a = a + x[i]
print(a)