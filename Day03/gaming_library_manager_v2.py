games = [
    {
        "title": "Ghost of Tsushima",
        "genre": "Action Adventure",
        "rating": 10
    },
    {
        "title": "Cyberpunk 2077",
        "genre": "RPG",
        "rating": 9
    },
    {
        "title": "Elden Ring",
        "genre": "Action RPG",
        "rating": 10
    }
]

def show_games():
    for game in games:
        print("Title:", game["title"])
        print("Genre:", game["genre"])
        print("Rating:", game["rating"])
        print("-------------------------")  # prints a separator line for better readability

show_games()
