# Write a function that takes a string as input and returns its corresponding ASCII representation as a list of integers.
# uses the ord() built in function will convert a character to its ASCII decimal integer ord=orderly as in order
# built in function chr() does the oposite

""" Example:
Input: "Hello"
Output: [72, 101, 108, 108, 111]
"""

input = "Hello"


def string_to_ascii(string) -> list[int]:
    """
    input string arg, converts to list of integers,
    uses the ord() built in function to return the corresponding
    ASCII decimal value for each char in the string in list format
    """
    lst = [ord(char) for char in string]
    return lst


# Test the function
input_str = "Hello"
print(string_to_ascii(input_str))
