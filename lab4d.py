# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: 07/10/2026
# Purpose: Create the complete calculator function using default parameters and positional parameters
# Usage: ./lab4d.py

# Follow the instructions from readme.md.
def compute(num1,num2,sym1):
    if sym1=="sub":
        return num1-num2
    elif sym1=="multi":
        return num1*num2
    elif sym1=="divi":
        return num1/num2
    else:
        return num1+num2

def main():
    num1=int(input("Please enter first number: "))
    num2=int(input("Please enter second number: "))
    sym1=(input("Please enter operation (+,-,*,/): "))
    result = compute(num1,num2,sym1)
    print(result)
if __name__ == "__main__":
    main()