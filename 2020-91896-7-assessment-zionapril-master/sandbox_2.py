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


shape_answer = []
#  *** Main Routine starts here ***
keep_going = ""
while keep_going == "":

    available_shapes = ["square", "rectangle", "triangle", "parallelogram", "circle", "trapezium"]
    calculator_1 = ["area", "perimeter", "area and perimeter"]
    # Asks user to choose what shape they want to work out
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

        unit = unit_checker()
        # makes sqaure_length a float
        square_length = float(square_length)
        # formula for area and perimeter of square
        area = square_length * square_length
        perimeter = square_length * 4
        # prints length to console
        print("The length is {} {}".format(square_length, unit))
        # prints area and perimeter of square
        print("The area of the square is {} {} squared".format(area, unit))
        print("The perimeter of the square is {} {}".format(perimeter, unit))
        # brief summary of information given in order for output
        shape_name = "Shape : {}".format(ask_user)
        display_dimensions_1 = "Area (Dimensions): {} {} x {} {}".format(square_length, unit, square_length, unit)
        display_dimensions_2 = "Perimeter (Dimensions): {} {} x 4".format(square_length, unit)
        display_area = "Area: {} {} squared".format(area, unit)
        display_perimeter = "Perimeter: {} {}".format(perimeter, unit)

        summary_1.append(shape_name)
        summary_1.append(display_dimensions_1)
        summary_1.append(display_dimensions_2)
        summary_1.append(display_area)
        summary_1.append(display_perimeter)

        print("*** Square Area / Perimeter ***")

    if ask_user == "rectangle":
        print("*** Rectangle Area / Perimeter ***")
        # Ask user for length and width of rectangle

        rectangle_length = num_check("What is the length:")
        rectangle_width = num_check("What is the width:")
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
        print("The area of the rectangle is {} {} squared".format(area, unit))
        print("The perimeter of the rectangle is {} {}".format(perimeter, unit))
        # brief summary of information given in order for output
        shape_name = "Shape: {}".format(ask_user)
        display_dimensions_1 = "Area(Dimensions): {} {} x {} {}".format(rectangle_width, unit, rectangle_length, unit)
        display_dimensions_2 = "Perimeter(Dimensions): {} {} + {} {} + {} {} + {} {}".format(rectangle_length, unit, rectangle_width, unit, rectangle_length, unit, rectangle_width, unit)
        display_area = "Area: {} {} squared".format(area, unit)
        display_perimeter = "Perimeter: {} {}".format(perimeter, unit)

        summary_1.append(shape_name)
        summary_1.append(display_dimensions_1)
        summary_1.append(display_dimensions_2)
        summary_1.append(display_area)
        summary_1.append(display_perimeter)

        print("*** Rectangle Area / Perimeter ***")

    if ask_user == "triangle":
        print("*** Triangle Area / Perimeter ***")
        # asks user if they want to work out A or P
        ask_user_1 = string_checker("Area or perimeter or Area and perimeter ? ", calculator_1)
        unit = unit_checker()
        # turns it into integer
        if ask_user_1 == "area":
            # Ask user for the necessary sides for triangle
            triangle_base = num_check("What is the base: ")
            perpendicular_height = num_check("What is the perpendicular height: ")
            # formula for area of triangle
            area = 0.5 * triangle_base * perpendicular_height
            # outputs area of triangle
            print("The Area of the triangle is {} {} squared".format(area, unit))
            # does not provide perimeter because never asked for it
            print("The perimeter of the triangle is N/A")
            # # brief summary of information given in order for output
            shape_name = "Shape: {}".format(ask_user)
            display_dimensions_1 = "Area(Dimensions): 0.5 x {} {} x {} {}".format(triangle_base, unit,
                                                                                  perpendicular_height, unit)
            display_dimensions_2 = "Perimeter is N/A"

            display_area = "Area: {} {} squared".format(area, unit)
            display_perimeter = "Perimeter: n/a"

            summary_1.append(shape_name)
            summary_1.append(display_dimensions_1)
            summary_1.append(display_dimensions_2)
            summary_1.append(display_area)
            summary_1.append(display_perimeter)

        if ask_user_1 == "perimeter":
            # asks user for necessary sides
            triangle_base = num_check("What is the base: ")
            triangle_height = num_check("What is slant height 1: ")
            triangle_height_2 = num_check("What is slant height 2:")
            # works out perimeter of triangle
            perimeter = triangle_base + triangle_height_2 + triangle_height
            # outputs perimeter of triangle
            print("The perimeter of the triangle is {} {}".format(perimeter, unit))
            # Area is N/A because user only asked for perimeter
            print("The Area of the triangle is N/A")
            # brief summary of information given in order for output
            shape_name = "Shape: {}".format(ask_user)
            display_dimensions_1 = "Area is N/A"
            display_dimensions_2 = "Perimeter(Dimensions): {} {} + {} {} + {} {}".format(triangle_base, unit,
                                                                                         triangle_height_2, unit,
                                                                                         triangle_height, unit)
            display_area = "Area: n/a"
            display_perimeter = "Perimeter: {} {}".format(perimeter, unit)

            summary_1.append(shape_name)
            summary_1.append(display_dimensions_1)
            summary_1.append(display_dimensions_2)
            summary_1.append(display_area)
            summary_1.append(display_perimeter)

        if ask_user_1 == "area and perimeter":
            # asks user for necessary sides
            triangle_base = num_check("What is the base: ")
            triangle_height = num_check("What is slant height 1: ")
            triangle_height_2 = num_check("What is slant height 2:")
            perpendicular_height = num_check("What is the perpendicular height: ")
            # becomes integer
            triangle_base = int(triangle_base)
            triangle_height = int(triangle_height)
            triangle_height_2 = int(triangle_height_2)
            perpendicular_height = int(perpendicular_height)
            # formula for area and perimeter of triangle
            area = 0.5 * triangle_base * perpendicular_height
            perimeter = triangle_base + triangle_height_2 + triangle_height
            # outputs area and perimeter of triangle
            print("The Area of the triangle is {} {} squared".format(area, unit))
            print("The perimeter of the triangle is {} {}".format(perimeter, unit))
            # brief summary of information given in order for output
            shape_name = "Shape: {}".format(ask_user)
            display_dimensions_1 = "Area(Dimensions): 0.5 x {} {} x {} {}".format(triangle_base, unit, perpendicular_height, unit)
            display_dimensions_2 = "Perimeter(Dimensions): {} {} + {} {} + {} {}".format(triangle_base, unit, triangle_height_2, unit,
                                                                             triangle_height, unit)
            display_area = "Area: {} {} squared".format(area, unit)
            display_perimeter = "Perimeter: {} {}".format(perimeter, unit)

            summary_1.append(shape_name)
            summary_1.append(display_dimensions_1)
            summary_1.append(display_dimensions_2)
            summary_1.append(display_area)
            summary_1.append(display_perimeter)

            print("*** Triangle Area / Perimeter ***")

    if ask_user == "circle":
        print("*** Circle Area / Circumference Solver ***")
        # Asks user for radius of circle
        circle_radius = num_check("What is the radius:")
        unit = unit_checker()
        # Turns string into integer
        circle_radius = int(circle_radius)
        # Works out area and circumference of circle
        area = 3.14 * circle_radius ** 2
        circumference = 2 * 3.14 * circle_radius
        circumference = int(circumference)
        # Displays area and circumference of circle
        print("The area is {} {} squared".format(area, unit))
        print("The circumference is {} {}".format(circumference, unit))

        # Rounded off numbers
        print(("Rounded off area is {}".format(round(area))))
        print(("Rounded off circumference is {}".format(round(circumference))))
        # brief summary of information given in order for output
        shape_name = "Shape: {}".format(ask_user)
        display_dimensions_1 = "Area(Dimensions): 3.14 x {} {} ^ 2".format(circle_radius, unit)
        display_dimensions_2 = "Circumference(Dimensions): 2 x 3.14 x {} {}".format(circle_radius, unit)
        display_area = "Area: {} {} squared".format(area, unit)
        display_perimeter = "Circumference: {} {}".format(circumference, unit)

        summary_1.append(shape_name)
        summary_1.append(display_dimensions_1)
        summary_1.append(display_dimensions_2)
        summary_1.append(display_area)
        summary_1.append(display_perimeter)

        print("*** Circle Area / Circumference Solver ***")

    if ask_user == "parallelogram":
        print("*** Parallelogram Area / Perimeter Solver ***")
        # asks user if they want to work out A or P
        ask_user_1 = string_checker("Area or perimeter or Area and perimeter ? ", calculator_1)
        # asks user for necessary length
        if ask_user_1 == "area":
            # Asks user for necessary lengths
            parallelogram_base = num_check("What is the base: ")
            parallelogram_height = num_check("what is the height:")
            unit = unit_checker()
            # formula for area of parallelogram
            area = parallelogram_base * parallelogram_height
            # outputs area of parallelogram
            print("The area of the parallelogram is {} {} squared".format(area, unit))
            # perimeter is N/A because only area is wanted
            print("The perimeter of the parallelogram is N/A")
            # brief summary of information given in order for output
            shape_name = "Shape: {}".format(ask_user)
            display_dimensions_1 = "Area(Dimensions): {} {} x {} {}".format(parallelogram_base, unit,
                                                                            parallelogram_height, unit)
            display_dimensions_2 = "Perimeter(Dimensions): n/a"
            display_area = "Area: {} {} squared".format(area, unit)
            display_perimeter = "Perimeter: n/a"

            summary_1.append(shape_name)
            summary_1.append(display_dimensions_1)
            summary_1.append(display_dimensions_2)
            summary_1.append(display_area)
            summary_1.append(display_perimeter)

        if ask_user_1 == "perimeter":
            # Asks user for necessary lengths
            parallelogram_base = num_check("What is the base: ")
            parallelogram_side = num_check("What is the side length:")
            unit = unit_checker()
            # formula for perimeter of parallelogram
            perimeter = 2 * (parallelogram_side + parallelogram_base)
            # outputs perimeter of parallelogram
            print("The perimeter of the parallelogram is {} {}".format(perimeter, unit))
            # area is N/A because only perimeter is wanted
            print("The area of the parallelogram is N/A")
            # brief summary of information given in order for output
            shape_name = "Shape: {}".format(ask_user)
            display_dimensions_1 = "Area(Dimensions): N/A"
            display_dimensions_2 = "Perimeter(Dimensions): 2 x ({} {} + {} {})".format(parallelogram_side, unit,
                                                                                       parallelogram_base, unit)
            display_area = "Area: N/A"
            display_perimeter = "Perimeter: {} {}".format(perimeter, unit)

            summary_1.append(shape_name)
            summary_1.append(display_dimensions_1)
            summary_1.append(display_dimensions_2)
            summary_1.append(display_area)
            summary_1.append(display_perimeter)

        if ask_user_1 == "area and perimeter":
            # Asks user for necessary lengths
            parallelogram_base = num_check("What is the base: ")
            parallelogram_height = num_check("what is the height:")
            parallelogram_side = num_check("What is the side length:")
            unit = unit_checker()
            # assigns to integer
            parallelogram_base = int(parallelogram_base)
            parallelogram_height = int(parallelogram_height)
            parallelogram_side = int(parallelogram_side)
            # formula for area of parallelogram
            area = parallelogram_base * parallelogram_height
            # formula for perimeter of parallelogram
            perimeter = 2 * (parallelogram_side + parallelogram_base)
            # returns the area and perimeter of parallelogram
            print("The area of the parallelogram is {} {} squared".format(area, unit))
            print("The perimeter of the parallelogram is {} {}".format(perimeter, unit))

            print("*** Parallelogram Area / Perimeter Solver ***")
            # brief summary of information given in order for output
            shape_name = "Shape: {}".format(ask_user)
            display_dimensions_1 = "Area(Dimensions): {} {} x {} {}".format(parallelogram_base, unit, parallelogram_height, unit)
            display_dimensions_2 = "Perimeter(Dimensions): 2 x ({} {} + {} {})".format(parallelogram_side, unit, parallelogram_base, unit)
            display_area = "Area: {} {} squared".format(area, unit)
            display_perimeter = "Perimeter: {} {}".format(perimeter, unit)

            summary_1.append(shape_name)
            summary_1.append(display_dimensions_1)
            summary_1.append(display_dimensions_2)
            summary_1.append(display_area)
            summary_1.append(display_perimeter)

    if ask_user == "trapezium":
        print("*** Trapezium Area / Perimeter ***")
        # asks user A or P or both
        ask_user_1 = string_checker("Area or perimeter or Area and perimeter ? ", calculator_1)
        # if user only wants to work out area
        if ask_user_1 == "area":
            # Asks user for necessary lengths
            bottom_base = num_check("What is the bottom base:")
            top_base = num_check("What is the top base:")
            height = num_check("What is the height:")
            unit = unit_checker()
            # formula for trapezium
            area = bottom_base + top_base / 2 * height
            # returns answer for area
            print("The area is {} {} squared".format(area, unit))
            # perimeter is N/A because only area is wanted
            print("The perimeter is N/A")
            # Brief summary for output
            shape_name = "Shape: {}".format(ask_user)
            display_dimensions_1 = "Area(Dimensions): {} {} + {} {} / 2 x {} {}".format(bottom_base, unit, top_base, unit,
                                                                                        height, unit)
            display_dimensions_2 = "Perimeter(Dimensions): N/A"

            display_area = "Area: {} {} squared".format(area, unit)
            display_perimeter = "Perimeter: n/a "

            summary_1.append(shape_name)
            summary_1.append(display_dimensions_1)
            summary_1.append(display_dimensions_2)
            summary_1.append(display_area)
            summary_1.append(display_perimeter)

        # if user only wants to work out perimeter
        if ask_user_1 == "perimeter":
            # asks user for necessary lengths
            bottom_base = num_check("What is the bottom base:")
            top_base = num_check("What is the top base:")
            side_1 = num_check("What is side 1:")
            side_2 = num_check("What is side 2:")
            unit = unit_checker()
            # formula for perimeter of trapezium
            perimeter = bottom_base + top_base + side_1 + side_2
            # returns answer for perimeter
            print("The perimeter is {} {}".format(perimeter, unit))
            # area is N/A because only perimeter is wanted
            print("The area is N/A")
            # brief summary for output
            shape_name = "Shape: {}".format(ask_user)
            display_dimensions_1 = "Area(Dimensions): n/a"
            display_dimensions_2 = "Perimeter(Dimensions): {} {} + {} {} + {} {} + {} {}".format(bottom_base, unit,
                                                                                                 top_base, unit,
                                                                                                 side_1, unit, side_2, unit)

            display_area = "Area: n/a"
            display_perimeter = "Perimeter: {} {}".format(perimeter, unit)

            summary_1.append(shape_name)
            summary_1.append(display_dimensions_1)
            summary_1.append(display_dimensions_2)
            summary_1.append(display_area)
            summary_1.append(display_perimeter)
        # if user wants to work out area and perimeter
        if ask_user_1 == "area and perimeter":
            # asks user for necessary lengths
            bottom_base = num_check("What is the bottom base:")
            top_base = num_check("What is the top base:")
            height = num_check("What is the height:")
            side_1 = num_check("What is side 1:")
            side_2 = num_check("What is side 2:")
            unit = unit_checker()
            # assigns to integer
            bottom_base = int(bottom_base)
            top_base = int(top_base)
            height = int(height)
            side_1 = int(side_1)
            side_2 = int(side_2)
            # formula for area of trapezium
            area = bottom_base + top_base / 2 * height
            # formula for perimeter of trapezium
            perimeter = bottom_base + top_base + side_1 + side_2
            # returns area and perimeter of trapezium
            print("The area is {} {} squared".format(area, unit))
            print("The perimeter is {} {}".format(perimeter, unit))

            print("*** Trapezium Area / Perimeter ***")
            # calculation summary for shape
            shape_name = "Shape: {}".format(ask_user)
            display_dimensions_1 = "Area(Dimensions): {} {} + {} {} / 2 x {} {}".format(bottom_base, unit, top_base, unit, height, unit)
            display_dimensions_2 = "Perimeter(Dimensions): {} {} + {} {} + {} {} + {} {}".format(bottom_base, unit, top_base, unit,
                                                                                     side_1, unit, side_2, unit)

            display_area = "Area: {} {} squared".format(area, unit)
            display_perimeter = "Perimeter: {} {}".format(perimeter, unit)

            summary_1.append(shape_name)
            summary_1.append(display_dimensions_1)
            summary_1.append(display_dimensions_2)
            summary_1.append(display_area)
            summary_1.append(display_perimeter)

    # gives the option to continue or quit

    keep_going = input("Press enter for another go or any key and then enter to quit")

    shape_answer.append(summary_1)
    # calculation summary
    print("***Calculation Summary***")
row = 0

# print(shape_answer)

for item in shape_answer:
    print(item[0])
    print(item[1])
    print(item[2])
    print(item[3])
    print(item[4])
    print()
    row += 1