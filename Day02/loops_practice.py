games = [
    "Ghost of Tsushima",
    "Cyberpunk 2077",
    "Elden Ring",
    "Red Dead Redemption 2",
    "GTA V"
]

for game in games:        # Loop through each game in the list
    print(game)

for game in games:
    print("I enjoy playing", game)       # Print a message for each game in the list

print("Total Games:", len(games))        # Print the total number of games in the list

#Python uses indentation (spaces at the beginning of a line) to decide what belongs to a loop.
#Anything that is indented under:

#for game in games:

#belongs to the loop.

#Python sees:

#for game in games:
#   print(game)
#   print("Done")
#as:
#Repeat these TWO statements
#for every game:
#Print the game
#Print "Done"
#So both statements run 3 times.