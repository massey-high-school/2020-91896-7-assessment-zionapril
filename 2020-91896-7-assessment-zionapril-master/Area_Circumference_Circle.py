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


print("*** Circle Area / Circumference Solver ***")

circle_radius = num_check("What is the radius:")

circle_radius = int(circle_radius)

area = 3.14 * circle_radius ** 2
circumference = 2 * 3.14 * circle_radius

print("The area is {}".format(area))
print("The circumference is {}".format(circumference))


# Rounded off numbers
print(("Rounded off area is {}".format(round(area))))
print(("Rounded off circumference is {}".format(round(circumference))))

print("*** Circle Area / Circumference Solver ***")