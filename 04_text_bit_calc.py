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

# calculates the # of bits for image (area x 8)
def img_bits():

    print()

    # aks user for image width and height
    img_width = num_check('How many pixels wide is your image? ')
    img_height = num_check('How many pixels tall is your imgae? ')

    # multiplies width and height
    img_pix = img_width * img_height
    # multiplies area by eight for bits
    img_bits = img_pix * 8

    print()
    print("Your image has an area of {} pixels.".format(img_pix))
    print("# of bits is {} x 8...".format(img_pix))
    print("We need {} bits to represent your image".format(img_bits))
    print()






