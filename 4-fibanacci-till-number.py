#!/usr/bin/env python3
"""
Give the user the full a Fibonacci series to a number when entered from the console.

Requirements:
- Input: A single integer number. The user must enter this from the console.
- Input validation:
  * Must be a valid integer number
  * Range: The number should be greater than or equal to 0 and less than or equal to 1 million (1,000,000).
- Input error handling:
  * If the input is not a valid integer, display an error message: "Invalid input: Please enter a valid integer number."
  * If the input is outside the specified range, display an error message: "Input out of range: Please enter a number between 0 and 1,000,000."
  * When invalid inout is provided then the user should be re-prompted to enter the number.
  * The standard CTRL+C interrupt should be accepted to exit the program.
- Output: A single line containing the Fibonacci series up to and including the entered number, with each number separated by a comma.
"""

def generate_fibonacci_series(limit):
  """
  Generate the Fibonacci series up to a specified limit.
  
  :param limit: The upper limit for the Fibonacci series
  :returns: A list containing the Fibonacci series up to the limit
  """
  fibonacci_series = []
  a, b = 0, 1
  while a <= limit:
    # De-dupe (eg. 1,1 should not appear)
    if b > a:
      fibonacci_series.append(a)
    a, b = b, a + b
  return fibonacci_series

def main():
  # Keep prompting until a valid integer within range is entered
  while True:
    try:
      user_input = input("Enter a number (0 to 1,000,000): ")
      number = int(user_input)

      if number < 0 or number > 1000000:
        print("ERROR: Input out of range: Please enter a number between 0 and 1,000,000.\n")
        continue

      # Valid input — break out of the loop
      break

    except ValueError:
      print("ERROR: Invalid input: Please enter a valid integer number.\n")
    except KeyboardInterrupt:
      print("\nExiting.")
      return

  # Generate and print the Fibonacci series
  fibonacci_series = generate_fibonacci_series(number)
  print("Fibonacci series up to", number, ":", ", ".join(map(str, fibonacci_series)))

if __name__ == "__main__":
  main()