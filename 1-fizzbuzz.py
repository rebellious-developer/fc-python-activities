#!/usr/bin/env python3
"""
Get “Fizz Buzz” for all numbers which can be divided by (3, 5,15). The range should from (1 to 100).

Requirements:
- Loop range is 1 to 100
- Anything divisible by 15 will print Fizzbuzz (note that these numbers are also divisible by 3 and 5)
- Anything divisible by 3 will print Fizz
- Anything divisible by 5 will print Buzz
- Anything not divisible by 3, 5 or 15 will print --
- Include the number in the output as a prefix
"""

def fizzbuzz():
  # Loop through numbers from 1 to 100
  for i in range(1, 101):
    # Check if divisible by 15 (both 3 and 5) first
    if i % 15 == 0:
      print(f"{i} : FizzBuzz")
    # Check if divisible by 3
    elif i % 3 == 0:
      print(f"{i} : Fizz")
    # Check if divisible by 5
    elif i % 5 == 0:
      print(f"{i} : Buzz")
    # If not divisible by 3, 5, or 15, print the number
    else:
      print(f"{i} : --")


if __name__ == "__main__":
  fizzbuzz()
