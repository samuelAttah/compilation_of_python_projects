try:
    num1 = float(input("Enter your number here: "))

    while num1 <= 10:
        print(num1)
        num1 += 1
except ValueError:
    print("input must be an integer")


secret_word = "Files"
guess = ""
count = 0
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if count < 3:
        guess = str(input("Enter your guess: "))
        count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You lose!, Try again Next Time")
else:
    print("You are correct")


def raise_to_power(base_num, power_num):
    result = base_num**power_num
    return result


print(raise_to_power(2, 3))



