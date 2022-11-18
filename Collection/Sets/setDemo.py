city = {"Bihar","Gao", "Delhi","UP","Bihar"}  #Duplicate Value not allowed, Order not maintain
citySet = set(("Les","Dubai", "Landon","Berlin","Denmark"))
city.add("Tamil Nadu")
citys = ["Les","Dubai", "Landon","Berlin","Denmark"]  #List
print(len(citys))
print(len(city))

print("List : " + citys[2])


print("Delhi" in city)
print(city)
newset = city.update(citySet)
print(city)
removeset = city.remove('Tamil Nadu')
print(city)