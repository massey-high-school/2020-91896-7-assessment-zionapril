# ask user for amount
# ask user for unit
# check that unit is dictionary

# Functions go here


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


# Main Routine goes here
unit_central = {
    "cm": 1,
    "m": 100,
    "mm": 0.1
}

keep_going = ""
while keep_going =="":
    amount = eval(input("How much? "))
    amount = float(amount)

    # Get unit and change it to match dictionary
    unit = unit_checker()

    if unit in unit_central:
        mult_by = unit_central.get(unit)
        amount = amount * mult_by
        print("Amount in cm {}".format(amount))
    else:
        print("{} is unchanged".format(amount))

    keep_going = input("<enter> or q ")



