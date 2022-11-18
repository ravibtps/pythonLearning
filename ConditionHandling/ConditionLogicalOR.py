data = input("Please a marks : ")
data = int(data)

if 100 < data < 0:
    print("INVAID MARKS")
else:
    if data < 40:
        print("Student is Fail")
    elif 40 < data < 60:
        print("3rd Division" + str(data))
    elif 60 < data < 80:
        print("2nd Division" + str(data))
    else:
        print("1st Division" + str(data))
