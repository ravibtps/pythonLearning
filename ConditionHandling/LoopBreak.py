number = input("Print the number : ")

for i in range(1, 15):
    if i == 11:
        break
    print(number + " * " + str(i) + " = " + str(i*int(number)))
