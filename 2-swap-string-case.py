#!/usr/bin/env python3
"""
Swap all uppercase characters in a user entered string to lowercase and vice versa.

Requirements:
- Input: A string containing both uppercase and lowercase characters. The user must enter this from the console.
- Output: A new string with uppercase characters converted to lowercase and lowercase characters converted to uppercase.
"""

def str_swap_case(input_string):
  # Initialize an empty string to store the result
  swapped_string = ""
  if input_string == "":
    return ""

  # Iterate through each character in the input string
  for char in input_string:
    # Check if the character is uppercase
    if char.isupper():
      # Convert to lowercase and add to result
      swapped_string += char.lower()
    # Check if the character is lowercase
    elif char.islower():
      # Convert to uppercase and add to result
      swapped_string += char.upper()
    else:
      # If it's not a letter, keep it unchanged
      swapped_string += char

  return swapped_string

def main():
  # Get user input from the console
  user_input = input("Enter a string: ")
  # Call the str_swap_case function and print the result
  result = str_swap_case(user_input)
  print("Swapped case string:", result)

if __name__ == "__main__":
  main()