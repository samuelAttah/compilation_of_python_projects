weight = input("weight: ")
converter = input("lbs or kg: ")
lbs = "l"
kg = "k"

if converter.upper() == lbs:
    print("your weight in kilogram is: ")
    print(10 * int(weight))

elif converter.upper() == kg:
    print("your weight in pounds is: ")
    print( 0.1 * int(weight))

