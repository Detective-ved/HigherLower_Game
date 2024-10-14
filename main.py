# imports
from game_data import data
from art import logo, vs
from replit import clear
import random

# Function to choose a new random player:
def choose_player():
    player = random.choice(data)
    p_name = player['name']
    p_follower = player['follower_count']
    p_desc = player['description']
    p_country = player['country']
    p_data = [p_name, p_desc, p_country, p_follower]
    return p_data

# Extracting player data:
def player_data(A, B):
    a = A[1][0]
    b = B[1][0]
    if a in 'aeiouAEIOU':
        print(f"Compare A: {A[0]}, an {A[1]}, from {A[2]}.")
    else:
        print(f"Compare A: {A[0]}, a {A[1]}, from {A[2]}.")
    print()
    print(vs)
    if b in 'aeiouAEIOU':
        print(f"Against B: {B[0]}, an {B[1]}, from {B[2]}.")
    else:
        print(f"Against B: {B[0]}, a {B[1]}, from {B[2]}.")

# shortcut renewal for turn:
def new_chance():
    clear()
    print(logo)

# comparing both players:
def check(A, B, score):
    a = A[3]
    b = B[3]
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if a != b:
        if choice == 'a':
            if a>b:
                score += 1
                new_chance()
                print(f"You're right! Current score: {score}.")
                B = choose_player()
            else:
                new_chance()
                print(f"Sorry, that's wrong. Final score: {score}.")
        elif choice == 'b':
            if b>a:
                score += 1
                new_chance()
                print(f"You're right! Current score: {score}.")
                A = B
                B = choose_player()
            else:
                new_chance()
                print(f"Sorry, that's wrong. Final score: {score}.")
    return score, A, B

# Final game
def game():
    player_A = choose_player()
    player_B = choose_player()
    score = 0
    clear()
    print(logo)
    print("You have only 3 lives.")
    lives = 3
    is_game_over = False
    while not is_game_over:
        player_data(player_A, player_B)
        final_data = check(player_A, player_B, score)
        if final_data[0] == score:
            print()
            play_again = input("Wanna play again? Type 'y' or 'n' : ").lower()
            print()
            if play_again == 'n':
                print("Game Over!")
                is_game_over = True
            else:
                lives -= 1
                if lives > 0:
                    print(f"You have {lives} lives remaining.")
                else:
                    is_game_over = True
        else:
            player_A = final_data[1]
            player_B = final_data[2]
            score = final_data[0]

game()