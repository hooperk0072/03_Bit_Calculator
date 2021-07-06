# calculates the # of bits for image (area x 8)
def img_bits():

    print()

    # aks user for image width and height
    img_width = num_check('How many pixels wide is your image? ')
    img_height = num_check('How many pixels tall is your imgae? ')

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



