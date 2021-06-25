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

def img_bits():

    print()
    # aks user for image width

    img_width



#checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid: 

        error = ('Please enter a number that is more than zero')

        try:

            # asks user to enter a number
            response = float(input(question))

            # checks if numer is more than zero
            if response > 0:
                return response

            # outputs error if numer is invalid
            else: 
                print(error)
                print()

        except ValueError:
            print(error)
            print()

#gets the width and height variables
img_width = num_check('How many pixels wide is your image? ')
img_height = num_check('How many pixels tall is your imgae? ')
