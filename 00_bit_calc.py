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

# displays instructions / information
def instructions():
    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose a file type (image / text / integer)")
    print()
    print("This program assumes that images are being represented in 24 bit colour (ie: 24 bits per pixel). For text, we assume that ascii encoding is being used (8 bits per character).")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
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

# calculates the # of bits for image (area x 8)
def img_bits():

    print()

    # aks user for image width and height
    img_width = num_check('How many pixels wide is your image? ', 1)
    img_height = num_check('How many pixels tall is your imgae? ', 1)

    # multiplies width and height for area/pixels
    img_pix = img_width * img_height

    # multiplies area/pixels by 24 for bits
    img_bits = img_pix * 24

    # output answer with working
    print()
    print("Your image has an area of {} pixels.".format(img_pix))
    print("The number of bits is {} x 24...".format(img_pix))
    print("We need {} bits to represent your image".format(img_bits))
    print()

#calculates the bits of an integer
def int_bits():


    # get integer (must be >= 0)
    var_integer = num_check("Please enter an integer: ", 0)

    var_binary = "{0:b}".format(var_integer)

    # calculate # of bits (length of string above)
    num_bits = len(var_binary)

    # output answer with working
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("Number of bits is {}".format(num_bits))
    print()

# calculates the # of bits for text (# of characters x 8)
def text_bits():

    print()
    # ask user for a string...
    var_text = input("Enter some text: ")

    # calculate # of bits (length of string x 8)
    var_length = len(var_text)
    num_bits = 8 * var_length

    # output answer with working
    print()
    print("\'{}\' has {} characters ...".format(var_text, var_length))
    print("# of bits is {} x 8...".format(var_length))
    print("We need {} bits to represent {}".format(num_bits, var_text))
    print()

    return ""

# displays instructions, information
def instructions():
    statement_generator("Instructions / Information", "-")

    print()
    print("Please choose a data type (image / text / integer)")
    print()
    print("This program assumes that images are being represented in 24 bit colour (ie: 24 bits per pixel). For text, we assume that ascii encoding is being used (8 bits per character).")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    print()
    return ""


# main routine
statement_generator("Bit Calculator for Integers, Text, and Images", "-")

instructions()

keep_going = ""
while keep_going == "":

    #ask the user for file type
    data_type = user_choice()
    print("You chose ", data_type)

    # for integers, ask for integer
    if data_type =="integer":
        int_bits()

    # for images, ask for width and height, must be integers more than/equal to 1
    elif data_type == "image":
        img_bits()
    
    # for text ask for a string
    else:
        text_bits()

