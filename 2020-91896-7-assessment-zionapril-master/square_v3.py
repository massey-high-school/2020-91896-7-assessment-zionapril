# functions goes here


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

# Main Routine
unit_central = {
    "cm": 1,
    "m": 100,
    "mm": 0.1
}

print("*** Square Area / Perimeter ***")
# Ask user length of square
keep_going = ""
while keep_going == "":
    square_length = num_check("What is the length: ")

    unit = unit_checker()

    square_length = float(square_length)

    area = square_length * square_length
    perimeter = square_length * 4

    print("The length is {} {}".format(square_length, unit))

    print("The area of the square is {} {}".format(area, unit))
    print("The perimeter of the square is {} {}".format(perimeter, unit))

    print("*** Square Area / Perimeter ***")
    keep_going = input("<enter> or q ")