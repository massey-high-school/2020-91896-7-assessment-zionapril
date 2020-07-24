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

rectangle_length = num_check("What is the length:")
rectangle_width = num_check("What is the width:")

rectangle_length = int(rectangle_length)
rectangle_width = int(rectangle_width)

area = rectangle_width * rectangle_length
perimeter = rectangle_length + rectangle_width + rectangle_length + rectangle_width

print("length:{}".format(rectangle_length))
print("width:{}".format(rectangle_width))

print("The area of the rectangle is {}".format(area))
print("The perimeter of the rectangle is {}".format(perimeter))

print("*** Rectangle Area / Perimeter ***")
