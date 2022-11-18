# a list of programming languages  Lists are created using square brackets:
LangList =['Python', 'C++', 'JavaScript',"C", 123, 23.0,"SQL"]
print(LangList)
print(len(LangList))

LangList[0]= "HTML"
print(LangList)

print("Last Word : " + str(LangList[-3]))
# print(LangList[-3])
# print(type(LangList))
#
# thislist = list(('Python', 'C++', 'JavaScript','C', 123, 23.0,'Python'))         # note the double round-brackets
# print(thislist)
# print(thislist[1])
#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#
#
thislist = ["apple", "banana", "cherry", "Laddu", "Laddu420", "Anti420", "RaviGreat"]

if "Laddu" in thislist:
    print("Yes, 'banana' is in the fruits list")
else:
    print("Not a fruit")