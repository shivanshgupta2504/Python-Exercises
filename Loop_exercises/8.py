"""
Display Fibonacci series up to 10 terms
"""

n = 10
num1 = 0
num2 = 1

for _ in range(n):
    print(num1, end=' ')

    res = num1 + num2
    num1 = num2
    num2 = res
