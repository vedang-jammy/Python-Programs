# this is the small program to learn loops
userInput = ""
carIsStarted = False
while True:
    userInput = input("> ").upper()
    if userInput == "START":
        if carIsStarted:
            print("Car is already started")
        else:
            carIsStarted = True
            print("The car started")
    elif userInput == "STOP":
        if not carIsStarted:
            print("Car is already stopped")
        else:
            carIsStarted = False
            print("The car stopped")
    elif userInput == "HELP":
        print(
            """
start - to start the car
stop - to stop the car
quit - to quit the game
             """
        )
    elif userInput == "QUIT":
        break
    else:
        print("I don't understand that")
