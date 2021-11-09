import random


def cube(num):
    result = num**3
    return result


print(cube(3))


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice1 = Dice()
print(dice1.roll())


num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1+num2)
elif op == "*":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
else:
    print("invalid operator")



