# this is my first mini project

weight = int(input("enter your weight: "))
unit = input("(L)bs or (K)g :")
if unit == "l" or unit == "L":
    # if unit.upper() == "L":
    weightInKg = weight * 0.45
    print(f"you are {int(weightInKg)} killograms.")
elif unit == "k" or unit == "K":
    # elif unit.upper() == "K":
    weightInLbs = weight // 0.45
    print(f"you are {weightInLbs} pounds.")
else:
    print("enter the correct unit.")
