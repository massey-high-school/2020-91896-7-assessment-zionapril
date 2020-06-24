# Functions goes here


def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("Can only be square, rectangle, triangle, parallelogram or circle")


#  *** Main Routine starts here ***

available_shapes = ["square", "rectangle", "triangle", "parallelogram", "circle"]

ask_user = string_checker("Choose a shape to work out:", available_shapes)
print(ask_user)

