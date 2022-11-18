# Key Value    Name:Laddu      Laptop: Dell {}  order Collection

Info = {"Ravi": [23, "Mumbai", "Thane"], "Bharat": [32, "Munarika", "IIT"], "Ram": 31}

print(Info["Bharat"])
print(Info.get("Ravi"))
print(Info.keys())
print(Info.values())
print(Info.items())

newValue = Info["Bharat"][2] = "NIT"
print(Info["Bharat"])

newValue = Info["Bharat"][2] = "Single"
print(Info["Bharat"])
Info["Ram"] = [24, "USA", "Married", "Child"]
Info.pop("Bharat")
print(Info.items())
