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

# Ask user length of square
length = num_check("What is the length: ")

length_1 = float(length)

area = length_1 * length_1
perimeter = length_1 * 4

print("The length is {}".format(length_1))

print("The area of the square is {}".format(area))
print("The perimeter of the square is {}".format(perimeter))