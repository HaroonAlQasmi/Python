import math

number1 = input("Enter First number:")
Operation = input("Enter Operation like + , - , /,e,* :")
number2 = input("Enter Second Number:")

if Operation == "+":
    print(int(number1) + int(number2))
if Operation == "-":
    print(float(number1) - float(number2))
if Operation == "/":
    print(float(number1) / float(number2))
if Operation == "e":
    print(pow(float(number1),float(number2)))
if Operation == "*":
    print(float(number1)*float(number2))
else:
    print("WRONG INPUT")