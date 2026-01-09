#!/usr/bin/env python3
"""
Swap two numbers showing it done with both a third variable and without a third variable.

Requirements:
- Input is hardcoded. A tuple of tuples with each item containing the two numbers that will be swapped.
- Output: Per two numbers to swap render the following:
  LINE 1: Showing what the two numbers are. Eg. A=45, B=78
  LINE 2: Show the result of the two numbers swapped using a third variable (eg. SwapWith3rdVar-Result: A=78, B=45)
  LINE 3: Show the two numbers swapped without using a third variable (SwapWithNoVar-Result: A=78, B=45)
  LINE 4: Show a blank line
"""

def swap_with_third_variable(a, b):
  """
  Uses a third variable to swap two numbers.
  
  :param a: The first number
  :param b: The second number
  :returns: A tuple containing the swapped numbers (a, b)
  """

  # A simple swap using a temporary variable
  temp = a
  a = b
  b = temp
  return a, b

def swap_without_third_variable(a, b):
  """
  Swap two numbers without using a third variable.
  
  :param a: The first number
  :param b: The second number
  :returns: A tuple containing the swapped numbers (a, b)
  """

  # Swap using tuple unpacking
  a, b = b, a
  return a, b

def main():
  # Hardcoded input: tuple of tuples
  numbers_to_swap = ((45, 78), (100, 200), (5, 10))

  for a, b in numbers_to_swap:
    print(f"A={a}, B={b}")
    
    # Swap using a third variable
    swapped_a, swapped_b = swap_with_third_variable(a, b)
    print(f"SwapWith3rdVar-Result: A={swapped_a}, B={swapped_b}")
    
    # Swap without using a third variable
    swapped_a, swapped_b = swap_without_third_variable(a, b)
    print(f"SwapWithNoVar-Result: A={swapped_a}, B={swapped_b}")
    
    print()  # Blank line

if __name__ == "__main__":
  main()