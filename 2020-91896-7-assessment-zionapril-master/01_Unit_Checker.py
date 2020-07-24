# Functions goes here
def unit_checker(preferred_unit):

    unit_to_check = preferred_unit

    # Abbreviation listssnip
    centimetres = ["cm", "centimetres"]
    metres = ["metres", "m"]
    millimetres = ["millimetres", "mm"]

    if unit_to_check == "":
        print("you chose {}".format(unit_to_check))
        return unit_to_check

    elif unit_to_check == "cm" or unit_to_check.lower() in centimetres:
        return "cm"
    elif unit_to_check.lower() in metres:
        return "m"
    elif unit_to_check.lower() in millimetres:
        return "mm"
    else:
        print(unit_to_check)
        return unit_to_check

ask_user = unit_checker("Whats your preferred unit:")

