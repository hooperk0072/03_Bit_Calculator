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
            want_intiger = input("Press <enter> for an integer or any key for an image.")
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
            # if response is not valid, outut an error
            print("Please chose a valid file type!")
            print()

# main routine
keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print("You chose", data_type)

    print()