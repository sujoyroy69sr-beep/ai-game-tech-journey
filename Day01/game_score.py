game_score = input("Enter your score: ")
if game_score.isdigit():
    game_score = int(game_score)
    if game_score >= 90:
        print("Legend")
    elif game_score >= 70:
        print("Advanced")
    elif game_score >= 50:
        print("Intermediate")
    else:
        print("Beginner")
else:
    print("Please enter a valid number.")