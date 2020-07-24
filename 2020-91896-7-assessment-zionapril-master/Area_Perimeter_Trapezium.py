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
                    return float(response)

            except ValueError:
                print(error)


# Main Routine

print("*** Trapezium Area / Perimeter ***")

bottom_base = num_check("What is the bottom base:")
top_base = num_check("What is the top base:")
height = num_check("What is the height:")
side_1 = num_check("What is side 1:")
side_2 = num_check("What is side 2:")


bottom_base = int(bottom_base)
top_base = int(top_base)
height = int(height)
side_1 = int(side_1)
side_2 = int(side_2)

area = bottom_base + top_base / 2 * height
perimeter = bottom_base + top_base + side_1 + side_2

print("The area is {}".format(area))
print("The perimeter is {}".format(perimeter))

print("*** Trapezium Area / Perimeter ***")
