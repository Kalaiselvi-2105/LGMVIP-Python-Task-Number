# -*- coding: utf-8 -*-
"""LGMVIP-Python-Task No:3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oLBt6oNul51pBMAgUdppsRCdzaTcOLNE
"""

import random
moves = ['rock', 'paper', 'scissors']
def get_user_move():
    user_move = input("Enter your move (rock, paper, scissors): ").lower()
    while user_move not in moves:
        print("Invalid move. Please try again.")
        user_move = input("Enter your move (rock, paper, scissors): ").lower()
    return user_move

def get_computer_move():
    return random.choice(moves)

def determine_winner(user_move, computer_move):
    if user_move == computer_move:
        return "It's a tie!"
    elif (user_move == 'rock' and computer_move == 'scissors') or \
         (user_move == 'paper' and computer_move == 'rock') or \
         (user_move == 'scissors' and computer_move == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    while True:
        user_move = get_user_move()
        computer_move = get_computer_move()

        print(f"\nYou chose: {user_move}")
        print(f"Computer chose: {computer_move}")

        result = determine_winner(user_move, computer_move)
        print(result)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

print("Welcome to Rock Paper Scissors!")
play_game()
print("Thanks for playing!")