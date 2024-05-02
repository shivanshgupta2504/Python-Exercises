"""
Calculate the sum of all numbers from 1 to a given number
"""

n = int(input("Enter a number: "))
sum = 0

for num in range(1, n+1):
    sum += num

print(f"Sum is {sum}")