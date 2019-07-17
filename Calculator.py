# Functional Calculator
import math

def add(num1, num2):
    return str(num1 + num2)


def subtract(num1, num2):
    return str(num1 - num2)


def multiply(num1, num2):
    return str(num1 * num2)


def divide(num1, num2):
    return str(num1 / num2)


def area_of_triangle(base, height):
    return str(base * height / 2)


def area_of_circle(radius):
    return str(math.pi * (radius * radius))


def inch_to_cm(inch):
    return str(2.54 * inch)


print('Welcome to my calculator!')
print('Please select an option from the list!')
print('1. Addition\n2. Subtraction\n3. Multiplication\n4. Division'
      '\n5. Area of triangle\n6. Area of circle\n7. Convert inches to cm')
choice = ''
while choice.isnumeric() == 0:
    choice = input('Please select an option: ')
if choice == '1':
    print('You chose addition')
    num1 = int(input('Please input the first number: '))
    num2 = int(input('Please input the second number: '))
    print('The total is: ' + add(num1, num2))
elif choice == '2':
    print('You chose subtraction')
    num1 = int(input('Please input the first number: '))
    num2 = int(input('Please input the second number: '))
    print('The total is: ' + subtract(num1, num2))
elif choice == '3':
    print('You chose multiplication')
    num1 = int(input('Please input the first number: '))
    num2 = int(input('Please input the second number: '))
    print('The total is: ' + multiply(num1, num2))
elif choice == '4':
    print('You chose division')
    num1 = int(input('Please input the first number: '))
    num2 = int(input('Please input the second number: '))
    print('The total is: ' + divide(num1, num2))
elif choice == '5':
    print('You chose area of a triangle')
    base = int(input('Please input the length of the base: '))
    height = int(input('Please input the heigh '))
    print('The area is: ' + area_of_triangle(base, height))
elif choice == '6':
    print('You chose area of a circle')
    r = int(input('Please input the radius: '))
    print('The radius is ' + area_of_circle(r))
elif choice == '7':
    print('You chose inches to cm converter')
    inch = int(input('Please input the length you wish to convert, in inches: '))
    print(f'{inch} inches is equivalent to {inch_to_cm(inch)}cm')
else:
    print("Sorry but that wasn't an option!")


