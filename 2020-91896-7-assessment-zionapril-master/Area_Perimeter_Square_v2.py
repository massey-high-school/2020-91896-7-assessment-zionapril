# Functions goes here


def num_check(question):

    error = "It should contain a number more than zero."

    valid = False
    while not valid:
        response = (input(question))

        if response.lower() == "xxx":
            return "xxx"

        else:
            try:
                if float(response) <=0:
                    print(error)
                else:
                    return response

            except ValueError:
                print(error)


# Main Routine
print("*** Square Area / Perimeter ***")
# Ask user length of square
square_length = num_check("What is the length: ")

square_length = float(square_length)

area = square_length * square_length
perimeter = square_length * 4

print("The length is {}".format(square_length))

print("The area of the square is {}".format(area))
print("The perimeter of the square is {}".format(perimeter))

print("*** Square Area / Perimeter ***")
