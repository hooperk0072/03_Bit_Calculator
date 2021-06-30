# Functions go here

# puts a series of symbols at start and end of text for emphasis
def statement_generator(text, decoration):

    # make string with five characters
    ends = decoration * 5

    # add decoration to start and end of a statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return""

# checks user choice is integer, text, or image
def user_choice():

    # lists valid responses
    text_ok = ["text", "t", "txt", "words", "string"]
    int_ok = ["integer", "intiger", "int", "#", "number", "num"]
    image_ok = ["image", "img", "pix", "pixels," "picture", "pic", "photo"]
    valid = False
    while not valid:
        # ask user for choice and change response to lowercase
        response = input("File type (integer / text / image): ").lower()

        # if they chose t or text, return text
        if response in text_ok:
            return "text"

        elif response in int_ok:
            return "integer"

        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for an image.")
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
            # if response is not valid, outut an error
            print("Please chose a valid file type!")
            print()

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

# calculates bits

# main routine

    statement_generator("This is a statement", "*")
    user_choice()

keep_going = ""
while keep_going == "":
    #ask the user for file type
    data_type = user_choice()
    print("You chose ", data_type)

    # for integers, ask for integer
    if data_type =="integer":
        var_integer = num_check("Enter an integer: ", 0)

    # for images, as for width and height
    # must be integers more than/equal to zero
    elif data_type == "image":
        print()
        image_width = num_check("Image width? ", 1)
        print()
        image_height = num_check("Image height? ", 1)
