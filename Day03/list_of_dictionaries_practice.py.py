games = [
    {
        "title": "Ghost of Tsushima",
        "rating": 10
    },
    {
        "title": "Cyberpunk 2077",
        "rating": 9
    }
]

for game in games:
    print(game["title"])    # prints the title of each game
    print(game["rating"])   # prints the rating of each game

# The for loop takes each dictionary in the list and assigns it to the variable 'game' in each iteration.
# For the first iteration, 'game' will be the dictionary {"title": "Ghost of Tsushima", "rating": 10}.
# For the second iteration, 'game' will be the dictionary {"title": "Cyberpunk 2077", "rating": 9}.

# So the output will be:
# Ghost of Tsushima
# 10
# Cyberpunk 2077
# 9