# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: 07/10/2026
# Purpose: use the main Function as entry point.
# Usage: ./lab4c.py

# Follow the instructions from readme.md.

def sum(num1,num2):
    return num1+num2

def main():
    num1=int(input("Please enter first number: "))
    num2=int(input("Please enter second number: "))
    result = sum(num1,num2)
    print(result)

if __name__ == "__main__":
    main()