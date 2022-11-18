number = input("Please enter the number : ")

for i in range(1, 11):
    if ((int(number))*i % 10) == 0:
        continue
    print(number + " * " + str(i) + " = " + str(i * int(number)))
