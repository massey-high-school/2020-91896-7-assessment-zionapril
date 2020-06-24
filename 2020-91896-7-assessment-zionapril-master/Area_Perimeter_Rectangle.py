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
print("*** Rectangle Area / Perimeter ***")
# Ask user for length and width of rectangle

length = num_check("What is the length:")
width = num_check("What is the width:")

length_2 = int(length)
width_1 = int(width)

area = width_1 * length_2
perimeter = length_2 + width_1 + length_2 + width_1

print("length:{}".format(length))
print("width:{}".format(width))

print("The area of the rectangle is {}".format(area))
print("The perimeter of the rectangle is {}".format(perimeter))

print("*** Rectangle Area / Perimeter ***")
