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
triangle_base = num_check("What is the base: ")
triangle_height = num_check("What is slant height 1: ")
triangle_height_2 = num_check("What is slant height 2:")
perpendicular_height = num_check("What is the perpendicular height: ")

triangle_base = int(triangle_base)
triangle_height = int(triangle_height)
triangle_height_2 = int(triangle_height_2)
perpendicular_height = int(perpendicular_height)

area = 0.5 * triangle_base * perpendicular_height
perimeter = triangle_base + triangle_height_2 + triangle_height

print("The Area of the triangle is {}".format(area))
print("The perimeter of the triangle is {}".format(perimeter))

print("*** Triangle Area / Perimeter ***")



