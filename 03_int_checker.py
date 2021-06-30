#checks input is a number more than a given value
def num_check(question, low):


    valid = False
    while not valid: 

        error = 'Please enter a number that is more than or equal to {}'.format(low)

        try:

            # asks user to enter a number
            response = int(input(question))

            # checks if numer is more than zero
            if response >= low:
                return response

            # outputs error if numer is invalid
            else: 
                print(error)
                print()

        except ValueError:
            print(error)
            print()

            keep_going = ""

while keep_going == "":
    print()
    # ask user for an integer (must be more than / equal to o)
    var_integer = num_check("Enter an integer: ", 0)
    print()
    # ask for width & height of an image
    # (must be more than / equal to 1)
    image_width = num_check("Image width? ", 1)
    print()
    image_height = num_check("Image height? ", 1)

