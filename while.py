command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started!!")
        else:
            started = True
            print("Car has started...")
    elif command == "stop":
        if not started:
            print("car is already stopped!!")
        else:
            started = False
            print("car has stopped...")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit the game
        """)
    elif command == "quit":
        break
    else:
        print("oops I don't understand that!!!")
