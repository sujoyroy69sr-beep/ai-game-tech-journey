player = {
    "name": "Kratos",
    "level": 50
}

print("Name:", player["name"])     # prints the value associated with the key "name" in the player dictionary, which is "Kratos"    

print("Level:", player["level"])   # prints the value associated with the key "level" in the player dictionary, which is 50

player["weapon"] = "Leviathan Axe"  #new key-value pair added to the dictionary

print("Weapon:", player["weapon"])  # prints the value associated with the key "weapon" in the player dictionary, which is "Leviathan Axe"

player["level"] = 51    # updates the value associated with the key "level" in the player dictionary to 51

print("Level:", player["level"])    # prints the updated value associated with the key "level" in the player dictionary, which is now 51
