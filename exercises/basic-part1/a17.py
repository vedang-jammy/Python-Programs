#Input a number, if it is not a number generate an error message

while True:
    try:
        num = int(input('enter a number:'))
        break
    except ValueError:
        print('this is not a number...try again.')
        print()
        