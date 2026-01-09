#!/usr/bin/env python3
"""
A small minimal number guessing game written in Python.

Requirements:
- The program should randomly select a number between 1 and 1000
- The user should be prompted to guess the number.
- After each guess, the program should inform the user if their guess was too low, too high, or correct.
- The game should continue until the user guesses the correct number, or until they have made X attempts or they decide to quit via CTRL+C
- Input validation:
  * The input must be a valid integer number.
  * The number must be within the range of 1 to 1000.
- Input error handling:
  * If the input is not a valid integer, display an error message: "Invalid input: Please enter a valid integer number."
  * If the input is outside the specified range, display an error message: "Input out of range: Please enter a number between 1 and 1000."
- The standard CTRL+C interrupt should be accepted to exit the program.
- Output:
  * Appropriate messages based on the user's guesses and the game's outcome.
  * If the user guesses correctly, display "YOU WIN!" (then exit)
  * If the user fails to guess the number within 5 attempts, display "YOU LOST. GAME OVER! The correct number was X." (then exit)
"""

import random

def main():
  min_num = 1
  max_num = 1000
  secret_number = random.randint(min_num, max_num)
  max_attempts = 10
  attempts = 0

  print("Welcome to the Number Guessing Game!")
  print(f"I have selected a number between {min_num} and {max_num}.")
  print(f"You have {max_attempts} attempts to guess the correct number.")
  print("Press CTRL+C to exit the game at any time.\n")

  while attempts < max_attempts:
    try:
      user_input = input(f"Attempt {attempts + 1}: Enter your guess: ")
      guess = int(user_input)

      if guess < min_num or guess > max_num:
        print(f"ERROR: Input out of range: Please enter a number between {min_num} and {max_num}.\n")
        continue

      attempts += 1

      if guess < secret_number:
        print("Your guess is too low.\n")
      elif guess > secret_number:
        print("Your guess is too high.\n")
      else:
        print("YOU WIN!")
        return

    except ValueError:
      print("ERROR: Invalid input: Please enter a valid integer number.\n")
    except KeyboardInterrupt:
      print("\nExiting the game. Goodbye!")
      return

  print(f"YOU LOST. GAME OVER! The correct number was {secret_number}.")

if __name__ == "__main__":
  main()