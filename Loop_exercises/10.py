"""
Calculate the cube of all numbers from 1 to a given number
"""

input_number = int(input("Enter the number: "))

for num in range(1, input_number+1):
    print(f"Current number: {num} and it's cube: {num**3}")

