price = 1000000
is_good_credit = False

if is_good_credit:
    print("You have a good credit record. Find below your payment details: ")
    print(price * 0.1)
else:
    print("You have a bad credit record. Find below your payment details:")
    print(price * 0.2)


