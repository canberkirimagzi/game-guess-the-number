#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def check(number, guess):
  if guess > number:
    print("Too high.")
    return False
  elif guess < number:
    print("Too low.")
    return False
  else:
    return True

def game(numbers_left, my_number):
  print(f"You have {numbers_left} attempts remaining to guess the number")
  guess = int(input("Make a guess: "))
  return check(my_number, guess)

def set_difficulty(difficulty):
  if difficulty == "easy":
    return 10
  elif difficulty == "hard":
    return 5
  else:
    print("Invalid input")
    return 0

from art import logo
print(logo) 

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

number_of_steps = set_difficulty(input("Choose a difficulty. Type 'easy' or 'hard': "))

import random
my_number = random.randint(1,100)

while number_of_steps > 0:
  if game(number_of_steps, my_number) == True:
    print(f"You got it! This answer was {my_number}.")
    break
  number_of_steps -= 1
  if number_of_steps == 0:
    print("You have run out of guesses, you lose.")
