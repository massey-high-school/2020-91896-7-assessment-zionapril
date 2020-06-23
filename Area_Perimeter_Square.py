# Functions goes here

# Not blank function goes here


def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in string and if its a number, complain
            for letter in response:
                if letter.isdigit():
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)

            continue
        else:
            return response

# Number checking function (number must be a float that is more than 0)


def num_check(question):

    error = "Please enter a number that is more than zero"

    valid = False

    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:

                return response

        except ValueError:
            print(error)


# Main Routine

# Ask user length and width of square
length = input("What is the length: ")
width = input("What is the width: ")

length_1 = int(length)
width_1 = int(width)

area = length_1 * width_1
perimeter = length_1 * 2 * width_1 * 2

print("The length is {}".format(length))
print("The width is {}".format(width))

print("The area of the square is {}".format(area))
print("The perimeter of the square is {}".format(perimeter))

