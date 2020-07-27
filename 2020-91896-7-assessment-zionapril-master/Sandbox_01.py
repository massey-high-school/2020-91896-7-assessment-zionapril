# Functions goes here

# string checker function


def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("Available list of shapes: "
              "* square",
              "* rectangle",
              "* triangle",
              "* parallelogram",
              "* circle",
              "* trapezium")

# number checking function


def num_check(question):

    error = "It should contain a number more than zero."

    valid = False
    while not valid:
        response = (input(question))

        if response.lower() == "xxx":
            return "xxx"

        else:
            try:
                if float(response) <= 0:
                    print(error)
                else:
                    return float(response)

            except ValueError:
                print(error)

# unit checking function


def unit_checker():

    unit_to_check = input("Unit? ")

    # Abbreviation listssnip
    centimeters = ["cm", "centimeters"]
    metres = ["m", "metres"]
    millimeters = ["mm", "millimeters"]

    if unit_to_check == "":
        print("you chose {}".format(unit_to_check))
        return unit_to_check

    elif unit_to_check == "cm" or unit_to_check.lower() in centimeters:
        return "cm"
    elif unit_to_check.lower() in metres:
        return "m"
    elif unit_to_check.lower() in millimeters:
        return "mm"
    else:
        return unit_to_check


#  *** Main Routine starts here ***
keep_going = ""
while keep_going == "":
    shape_answer = []
    available_shapes = ["square", "rectangle", "triangle", "parallelogram", "circle", "trapezium"]

    ask_user = string_checker("Choose a shape to work out:", available_shapes)
    print(ask_user)
    summary_1 = []

    unit_central = {
    "cm": 1,
    "m": 100,
    "mm": 0.1
}
# If shape is chosen
    if ask_user == "square":
        print("*** Square Area / Perimeter ***")
        # Ask user length of square
        square_length = num_check("What is the length: ")
        print("Available units:CM, M, MM")
        unit = unit_checker()
        # turns integer to string
        square_length = float(square_length)
        # works out area and perimeter of square
        area = square_length * square_length
        perimeter = square_length * 4
        # displays length of the square
        print("The length is {} {}".format(square_length, unit))
        # displays area and perimeter of the square
        print("The area of the square is {} {}".format(area, unit))
        print("The perimeter of the square is {} {}".format(perimeter, unit))
        summary_1.append(ask_user)
        summary_1.append(square_length)
        summary_1.append(unit)
        summary_1.append(area)
        summary_1.append(perimeter)

        print("*** Square Area / Perimeter ***")

    if ask_user == "rectangle":
        print("*** Rectangle Area / Perimeter ***")
        # Ask user for length and width of rectangle

        rectangle_length = num_check("What is the length:")
        rectangle_width = num_check("What is the width:")
        print("Available units:CM, M, MM")
        unit = unit_checker()
        # takes the decimal out and turns it into integer
        rectangle_length = int(rectangle_length)
        rectangle_width = int(rectangle_width)
        # works out area and perimeter of rectangle
        area = rectangle_width * rectangle_length
        perimeter = rectangle_length + rectangle_width + rectangle_length + rectangle_width
        # displays length and width of rectangle
        print("length:{} {}".format(rectangle_length, unit))
        print("width:{} {}".format(rectangle_width, unit))
        # displays area and perimeter of rectangle
        print("The area of the rectangle is {} {}".format(area, unit))
        print("The perimeter of the rectangle is {} {}".format(perimeter, unit))
        summary_1.append(ask_user)
        summary_1.append(rectangle_length)
        summary_1.append(rectangle_width)
        summary_1.append(unit)
        summary_1.append(area)
        summary_1.append(perimeter)

        print("*** Rectangle Area / Perimeter ***")

    if ask_user == "triangle":
        print("*** Triangle Area / Perimeter ***")
        # Ask user for the neccessary sides for triangle
        triangle_base = num_check("What is the base: ")
        triangle_height = num_check("What is slant height 1: ")
        triangle_height_2 = num_check("What is slant height 2:")
        perpendicular_height = num_check("What is the perpendicular height: ")
        print("Available units:CM, M, MM")
        unit = unit_checker()
        # turns it into integer
        triangle_base = int(triangle_base)
        triangle_height = int(triangle_height)
        triangle_height_2 = int(triangle_height_2)
        perpendicular_height = int(perpendicular_height)
        # works out area and perimeter of triangle
        area = 0.5 * triangle_base * perpendicular_height
        perimeter = triangle_base + triangle_height_2 + triangle_height
        # displays area and perimeter of triangle
        print("The Area of the triangle is {} {}".format(area, unit))
        print("The perimeter of the triangle is {} {}".format(perimeter, unit))
        summary_1.append(ask_user)
        summary_1.append(triangle_base)
        summary_1.append(triangle_height)
        summary_1.append(triangle_height_2)
        summary_1.append(unit)
        summary_1.append(perpendicular_height)
        summary_1.append(area)
        summary_1.append(perimeter)

        print("*** Triangle Area / Perimeter ***")

    if ask_user == "circle":
        print("*** Circle Area / Circumference Solver ***")
        # Asks user for radius of circle
        circle_radius = num_check("What is the radius:")
        print("Available units:CM, M, MM")
        unit = unit_checker()
        # Turns string into integer
        circle_radius = int(circle_radius)
        # Works out area and circumference of circle
        area = 3.14 * circle_radius ** 2
        circumference = 2 * 3.14 * circle_radius
        # Displays area and circumference of circle
        print("The area is {} {}".format(area, unit))
        print("The circumference is {} {}".format(circumference, unit))

        # Rounded off numbers
        print(("Rounded off area is {}".format(round(area))))
        print(("Rounded off circumference is {}".format(round(circumference))))

        shape_answer.append(ask_user)
        shape_answer.append(circle_radius)
        shape_answer.append(unit)
        shape_answer.append(area)
        shape_answer.append(circumference)

        print("*** Circle Area / Circumference Solver ***")

    if ask_user == "parallelogram":
        print("*** Parallelogram Area / Perimeter Solver ***")

        parallelogram_base = num_check("What is the base: ")
        parallelogram_height = num_check("what is the height:")
        parallelogram_side = num_check("What is the side length:")
        print("Available units:CM, M, MM")
        unit = unit_checker()

        parallelogram_base = int(parallelogram_base)
        parallelogram_height = int(parallelogram_height)
        parallelogram_side = int(parallelogram_side)

        area = parallelogram_base * parallelogram_height
        perimeter = 2 * (parallelogram_side + parallelogram_base)

        print("The area of the parallelogram is {} {}".format(area, unit))
        print("The perimeter of the parallelogram is {} {}".format(perimeter, unit))

        print("*** Parallelogram Area / Perimeter Solver ***")

        summary_1.append(ask_user)
        summary_1.append(parallelogram_base)
        summary_1.append(parallelogram_height)
        summary_1.append(parallelogram_side)
        summary_1.append(unit)
        summary_1.append(area)
        summary_1.append(perimeter)

    if ask_user == "trapezium":
        print("*** Trapezium Area / Perimeter ***")

        bottom_base = num_check("What is the bottom base:")
        top_base = num_check("What is the top base:")
        height = num_check("What is the height:")
        side_1 = num_check("What is side 1:")
        side_2 = num_check("What is side 2:")
        print("Available units:CM, M, MM")
        unit = unit_checker()

        bottom_base = int(bottom_base)
        top_base = int(top_base)
        height = int(height)
        side_1 = int(side_1)
        side_2 = int(side_2)

        area = bottom_base + top_base / 2 * height
        perimeter = bottom_base + top_base + side_1 + side_2

        print("The area is {} {}".format(area, unit))
        print("The perimeter is {} {}".format(perimeter, unit))

        print("*** Trapezium Area / Perimeter ***")

        keep_going = input("<enter> or q ")

        keep_going = input("<enter> or q ")

        summary_1.append(ask_user)
        summary_1.append(bottom_base)
        summary_1.append(top_base)
        summary_1.append(height)
        summary_1.append(side_1)
        summary_1.append(side_2)
        summary_1.append(unit)
        summary_1.append(area)
        summary_1.append(perimeter)

    shape_answer.append(summary_1)

    keep_going = input("Press enter for another go or any key and then enter to quit")

    # Calculation Summary

    if ask_user == "square":

        for square in shape_answer:
            print("***Calculation Summary***")
            print("shape: {}".format(square[0]))
            print("length: {} {}".format(square[1], square[2]))
            print("area: {} {} ".format(square[3], square[2]))
            print("perimeter: {} {}".format(square[4], square[2]))

    if ask_user == "rectangle":

        for rectangle in shape_answer:
            print("***Calculation Summary***")
            print("shape: {}".format(rectangle[0]))
            print("length: {} {}".format(rectangle[1], rectangle[3]))
            print("width: {} {}".format(rectangle[2], rectangle[3]))
            print("area: {} {}".format(rectangle[4], rectangle[3]))
            print("perimeter {} {}".format(rectangle[5], rectangle[3]))

    if ask_user == "triangle":

        for triangle in shape_answer:
            print("***Calculation Summary***")
            print("shape: {}".format(triangle[0]))
            print("base: {} {}".format(triangle[1], triangle[4]))
            print("height 1: {} {}".format(triangle[2], triangle[4]))
            print("height 2: {} {}".format(triangle[3], triangle[4]))
            print("perpendicular height: {} {}".format(triangle[5], triangle[4]))
            print("area: {} {}".format(triangle[6], triangle[4]))
            print("perimeter: {} {}".format(triangle[7], triangle[4]))

    if ask_user == "circle":

        for circle in shape_answer:
            print("***Calculation Summary***")
            print("shape: {}".format(circle[0]))
            print("radius: {} {}".format(circle[1], circle[2]))
            print("area: {} {}".format(circle[3], circle[2]))
            print("circumference: {} {}".format(circle[4], circle[2]))

    if ask_user == "parallelogram":

        for parallelogram in shape_answer:
            print("***Calculation Summary***")
            print("shape: {}".format(parallelogram[0]))
            print("base: {} {}".format(parallelogram[1], parallelogram[4]))
            print("height: {} {}".format(parallelogram[2], parallelogram[4]))
            print("side: {} {}".format(parallelogram[3], parallelogram[4]))
            print("area: {} {}".format(parallelogram[5], parallelogram[4]))
            print("perimeter: {} {}".format(parallelogram[6], parallelogram[4]))

    if ask_user == "trapezium":

        for trapezium in shape_answer:
            print("***Calculation Summary***")
            print("shape: {}".format(trapezium[0]))
            print("bottom base: {} {}".format(trapezium[1], trapezium[6]))
            print("top base: {} {}".format(trapezium[2], trapezium[6]))
            print("height: {} {}".format(trapezium[3], trapezium[6]))
            print("side 1: {} {}".format(trapezium[4], trapezium[6]))
            print("side 2: {} {}".format(trapezium[5], trapezium[6]))
            print("area: {} {}".format(trapezium[7], trapezium[6]))
            print("perimeter: {} {}".format(trapezium[8], trapezium[6]))
