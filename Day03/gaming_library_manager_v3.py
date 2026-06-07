games = []                  # Start with an empty list to store game information

def add_game():             # Function to add a new game to the library
    title = input("Enter the title of the game: ")
    genre = input("Enter the genre of the game: ")
    rating = int(input("Enter the rating of the game (1-10): "))

    new_game = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    games.append(new_game)
    print(f"{title} has been added to your library!")

def view_games():           # Function to display all games in the library
    if not games:
        print("Your game library is empty.")
    else:
        for game in games:
            print(f"Title: {game['title']}")
            print(f"Genre: {game['genre']}")
            print(f"Rating: {game['rating']}")
            print("-------------------")

def show_total_games():     # Function to show the total number of games in the library
    print(f"Total games in your library: {len(games)}")

print("Welcome to the Gaming Library Manager!\n"
      "You can view your game library, add new games, and manage your collection.\n"
      "What would you like to do?\n"
      "1. Add a new game\n"
      "2. View your game library\n"
      "3. Show total number of games")  # Prints a welcome message and presents the user with options to manage their gaming library

choice = input("Enter your choice (1-3): ")   # Takes the user's input to determine which action they want to perform in the gaming library manager. The user is expected to enter a number between 1 and 3, corresponding to the options presented in the welcome message.

if choice == "1":                               # If the user chooses option 1, the add_game() function is called to allow the user to add a new game to their library.
    add_game()
elif choice == "2":                         # If the user chooses option 2, the view_games() function is called to display all the games currently in their library.    
    view_games()
elif choice == "3":                 # If the user chooses option 3, the show_total_games() function is called to display the total number of games in their library.    
    show_total_games()
else:                             # If the user enters an invalid choice (anything other than 1, 2, or 3), a message is printed to inform them that their input is invalid and prompts them to enter a valid number between 1 and 3.
    print("Invalid choice. Please enter a number between 1 and 3.")
