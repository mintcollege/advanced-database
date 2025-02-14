"""
   *
  ***
 *****
*******
"""

"""
PSEUDO CODE for the half-triangle:

1. Find out how many rows do I need?
2. Find out how many spaces to show
3. Find out how many * to show
4. Know when to stop printing the *
"""
for i in range(5):
    stars = ''
    for j in range(i+1):
        stars += '@'
    print(stars)