# We will write a rock paper scissors game in class - Complete it in this file
# We will write a rock paper scissors game in class - Complete it in this file
import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'player'
    else:
        return 'computer'

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    print("Choose rock, paper, or scissors:")
    
    player_choice = input().lower()
    
    if player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    winner = get_winner(player_choice, computer_choice)
    
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'player':
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    play_game()
