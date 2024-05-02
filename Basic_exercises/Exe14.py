"""
Print a downward Half-Pyramid Pattern of Star (asterisk)
* * * * *  
* * * *  
* * *  
* *  
*
"""

for x in range(5, 0, -1):
    for y in range(0, x):
        print('*', end=' ')
    print()
