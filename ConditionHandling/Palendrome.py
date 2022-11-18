palendrome = input("Enter the palendrome word : ")

a = ""

l = len(palendrome)

for i in range(l - 1, -1, -1):
    a = a + palendrome[i]
print(a)

if palendrome == a:
    print("This word is palendrome word")
else:
    print("This word is not a palendrome word")
