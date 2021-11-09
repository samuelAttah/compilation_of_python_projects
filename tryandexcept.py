try:
    age = int(input("age: "))
    income = 20000
    risk = income/age
    print(risk)
except ZeroDivisionError:
    print("age can't be null")
except ValueError:
    print("Invalid Input")



