# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: 07/10/2026
# Purpose: Create Some Complex Functions.
# Usage: ./lab4b.py

# TO DO 1: Add the docstring
# @Function definition: add definition here
# @param: write parameters here
# @return: write return value here

# TO DO 2: Create the function.
lstall=[1,2,3,7,88,22,55]
def even_numbers(list1):
    lsteven=[]
    for i in list1:
        if i%2==0:
            lsteven.append(i)
    return lsteven
# TO DO 3: Call the function.
print (even_numbers(lstall))

