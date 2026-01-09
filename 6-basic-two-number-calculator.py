#!/usr/bin/env python3
"""
A small minimal calculator that takes two numbers and an operator from the user and performs the calculation.

Requirements:
- Input:
  * Two numbers (integers or floats) entered by the user via the console.
  * An operator entered by the user via the console. Supported operators are: +, -, *, /
- Output:
  * The result of the calculation displayed on the console.
- Input validation:
  * The numbers must be valid integers or floats.
  * The operator must be one of the supported operators.
- Input error handling:
  * If the input numbers are not valid, display an error message: "Invalid input: Please enter valid numbers."
  * If the operator is not supported, display an error message: "Invalid operator: Please enter one of +, -, *, /."
  * If division by zero is attempted, display an error message: "Error: Division by zero is not allowed."
- Other considerations:
  * Division by zero must be handled gracefully.
- The standard CTRL+C interrupt should be accepted to exit the program.
"""
def calculate(num1, num2, operator):
  """
  Perform a calculation based on the provided operator.
  
  :param num1: The first number (int or float)
  :param num2: The second number (int or float)
  :param operator: The operator as a string ('+', '-', '*', '/')
  :returns: The result of the calculation
  :raises ValueError: If the operator is invalid or division by zero is attempted
  """
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    if num2 == 0:
      raise ValueError("Error: Division by zero is not allowed.")
    return num1 / num2
  else:
    raise ValueError("Invalid operator: Please enter one of +, -, *, /.")
  
def main():
  while True:
    try:
      # Get user input
      num1_input = input("Enter the first number: ")
      num2_input = input("Enter the second number: ")
      operator = input("Enter an operator (+, -, *, /): ")

      # Convert inputs to float
      num1 = float(num1_input)
      num2 = float(num2_input)

      # Perform calculation
      result = calculate(num1, num2, operator)

      # Display result
      print(f"The result of {num1} {operator} {num2} is: {result}\n")

    except ValueError as ve:
      print(f"ERROR: {ve}\n")
    except KeyboardInterrupt:
      print("\nExiting the calculator. Goodbye!")
      return

if __name__ == "__main__":
  main()