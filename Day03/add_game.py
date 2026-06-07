new_game = {}

title = input("Enter the title of the game: ")
genre = input("Enter the genre of the game: ")
rating = int(input("Enter the rating of the game (1-10): "))

new_game["title"] = title
new_game["genre"] = genre
new_game["rating"] = rating

print("Title:", new_game["title"])
print("Genre:", new_game["genre"])
print("Rating:", new_game["rating"])