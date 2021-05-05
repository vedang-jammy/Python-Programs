# Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number

cubes = []
def cube_of_numbers(number):
    for num in range(1,number+1):
        result = num**3
        cubes.append(result)
    return cubes

number = int(input('Enter the positive integer:'))

print('cubes of numbers is:',cube_of_numbers(number))