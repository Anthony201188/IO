#Write a function that takes a hexadecimal string as input and returns its decimal (integer) value.
#uses the built in function of int(int ,to_the_base_of)

"""
Example:
Input: "1A"
Output: 26 
"""

def hex_to_int(hex)->int:
    """ Converts a hexadecimal number into an decimal integer """

    integer = int(hex, 16) # casts the varialbe as an int with a base of 16
    return integer


# Test the function
hex_str = "1A"
print(hex_to_int(hex_str))