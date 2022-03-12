import math


def calc_reminder(num1, num2):
    """function that return the reminder mod of two numbers"""
    return num1 % num2


def rounded_num(numbers):
    """function that return the rounded number"""
    return [round(i) for i in numbers]


def square_num(numbers):
    """function that return the sqrt of numbers"""
    return [math.sqrt(i) for i in numbers]


def power_num(numbers):
    """function that return the power of numbers"""
    return [i ** 2 for i in numbers]


def average(numbers):
    """function that return the average of numbers"""
    return sum(numbers) / len(numbers)


def min_num(numbers):
    """function that return max number"""
    return min(numbers)


def max_num(numbers):
    """function that return max number"""
    return max(numbers)


def sum_nums(numbers):
    """function that sum numbers"""
    return sum(numbers)


def get_numbers():
    """function to get numbers and add them to list, and check the validation of numbers"""

    choice = input('How many numbers you want to calculate? ')
    numbers = []
    try:
        choice = eval(choice)
        while choice > 0:

            try:
                number = eval(input('Enter number: '))
                numbers.append(number)

            except:  # return false if input was wrong
                return False

            choice -= 1
    except:  # return false if choice was wrong
        return False

    if numbers:
        return numbers
    else:  # return false if numbers lisr was empty
        return False


def menu():
    """menu function that starts the program"""
    print(
        '\nMenu:\nEnter 1 to sum numbers\nEnter 2 to get max number of numbers\nEnter 3 to get min number of numbers\nEnter 4 to get the average of numbers\nEnter 5 to get power for number of numbers\nEnter 6 to get the sqrt for number of numbers\nEnter 7 to get rounded number of numbers\n 0 to Quit')
    user = input(': ')

    while user != '0':
        # make sure that user choice is a correct number
        if user.isdecimal() and user in ['1', '2', '3', '4', '5', '6', '7']:
            # get numbers list
            numbers = get_numbers()

            if numbers:
                if user == '1':
                    print("The sum of numbers is: ", sum_nums(numbers))

                elif user == '2':
                    print("The Max number of numbers", numbers, 'is: ', max_num(numbers))

                elif user == '3':
                    print("The Min number of numbers", numbers, 'is: ', min_num(numbers))

                elif user == '4':
                    print("The Average of numbers", numbers, 'is: ', average(numbers))

                elif user == '5':
                    print("The Power number of numbers", numbers, 'is: ', power_num(numbers))

                elif user == '6':
                    print("The Sqrt number of numbers", numbers, 'is: ', square_num(numbers))

                elif user == '7':
                    print("The Rounded number of numbers", numbers, 'is: ', rounded_num(numbers))

            else:
                print('Please Enter a valid numbers')

        elif user.isdecimal() and user == '8':
            try:
                num1 = eval(input('Enter number 1: '))
                num2 = eval(input('Enter number 2: '))
                print('The reminder mod of numbers is: ', calc_reminder(num1, num2))
            except:
                print('Numbers was wrong!')

        else:
            print('Please Enter a valid choice')

        print(
            '\nMenu:\nEnter 1 to sum numbers\nEnter 2 to get max number of numbers\nEnter 3 to get min number of numbers\nEnter 4 to get the average of numbers\nEnter 5 to get power for number of numbers\nEnter 6 to get the sqrt for number of numbers\nEnter 7 to get rounded number of numbers\nEnter 8 to calculate reminder mod of two numbers\n Enter 0 to Quit')
        user = input(': ')

    print('Thanks for using our program**')


# start program
print('*' * 30, 'Welcome to our program', '*' * 30)
menu()