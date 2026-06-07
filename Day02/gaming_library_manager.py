games = [
    "Ghost of Tsushima",
    "Cyberpunk 2077",
    "Elden Ring"
]

def show_games():                               # Define a function to show the games
    for game in games:
        print(game)

def show_total_games():                         # Define a function to show the total number of games
    print("Total Games:", len(games))

show_games()                                    # Call the function to show the games
show_total_games()                              # Call the function to show the total number of games