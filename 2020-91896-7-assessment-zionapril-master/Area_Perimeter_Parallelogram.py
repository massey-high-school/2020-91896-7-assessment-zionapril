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

print("*** Parallelogram Area / Perimeter Solver ***")

parallelogram_base = num_check("What is the base: ")
parallelogram_height = num_check("what is the height:")
parallelogram_side = num_check("What is the side length:")


parallelogram_base = int(parallelogram_base)
parallelogram_height = int(parallelogram_height)
parallelogram_side = int(parallelogram_side)


area = parallelogram_base * parallelogram_height
perimeter = 2 * (parallelogram_side + parallelogram_base)

print("The area of the parallelogram is {}".format(area))
print("The perimeter of the parallelogram is {}".format(perimeter))

print("*** Parallelogram Area / Perimeter Solver ***")




