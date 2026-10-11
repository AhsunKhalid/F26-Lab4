# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: 07/10/2026
# Purpose: Modify the calcualtor program to use keyword parameters.
# Usage: ./lab4e.py

# Follow the instructions from readme.md.
def compute(num1,num2,sym1):
    if sym1=="-":
        return f"{num1}-{num2}"
    elif sym1=="*":
        return f"{num1}*{num2}"
    elif sym1=="/":
        return f"{num1}/{num2}"
    else:
        return f"{num1}+{num2}"

def main():
    num1=(input("Please enter first keyword: "))
    num2=(input("Please enter second keyword: "))
    sym1=(input("Please enter operation (+,-,*,/): "))
    result = compute(num1,num2,sym1)
    print(result)
if __name__ == "__main__":
    main()