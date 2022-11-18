# Key Value    Name:Laddu      Laptop: Dell {}  order Collection

Info = {"Ravi": [23,"Mumbai","Married"], "Laddu": [32,"Munarika","Randva"], "Guddu": 31}
print(Info["Laddu"])
print("Laddu Statu : " + Info["Laddu"][2])
print(Info["Guddu"])
print(Info.get("Ravi"))

print(Info.keys())
print(Info.values())
print(Info.items())

newValue = Info["Laddu"][2] = "Single"
print(Info["Laddu"])

Info["RamLagun"] = [87,"USA","Married","Child"]
Info.pop("Laddu")
print(Info.items())

