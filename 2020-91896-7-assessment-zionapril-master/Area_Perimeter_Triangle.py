# Functions goes here
from builtins import int


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

# Main Routine goes here

print("*** Triangle Area / Perimeter ***")
base = num_check("What is the base: ")
height = num_check("What is slant height 1: ")
height_2 = num_check("What is slant height 2:")
perpendicular_height = num_check("What is the perpendicular height: ")

base = int(base)
height = int(height)
height_2 = int(height_2)
perpendicular_height = int(perpendicular_height)

area = 0.5 * base * perpendicular_height
perimeter = base + height_2 + height

print("The Area of the triangle is {}".format(area))
print("The perimeter of the triangle is {}".format(perimeter))

print("*** Triangle Area / Perimeter ***")



