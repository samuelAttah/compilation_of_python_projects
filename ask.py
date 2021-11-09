name = input("what is your name?: ")


if len(name) <= 3:
    print("name is too short")
elif len(name) >= 50:
    print("name is too long")
else:
    print("successfully updated")
