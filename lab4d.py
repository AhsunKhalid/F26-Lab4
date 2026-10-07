# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Create the complete calculator function using default parameters and positional parameters
# Usage: ./lab4d.py

# Follow the instructions from readme.md.

def compute(num1,num2,sym1):
    if sym1=="-":
        return num1-num2
    elif sym1=="*":
        return num1*num2
    else:
        return num1+num2