"""
Write a program to print the following start pattern using the for loop

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""

for i in range(0, 5):
    for j in range(0, i+1):
        print('*', end=' ')
    print()

for i in range(4, 0, -1):
    for j in range(0, i):
        print('*', end=' ')
    print()
