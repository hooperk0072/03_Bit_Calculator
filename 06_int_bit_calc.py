# converts decimals to binary and states 
# how many bits are needed to represent the original integer
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

