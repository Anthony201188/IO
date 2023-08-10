#Write a function that takes an integer as input and returns its binary representation as a string.
#uses the built in function bin()

""" 
Example
Input: 42
Output: "101010"
"""

def int_to_binary(integer)-> str:
     """ takes an integer as an argument and converts it to binary """

     binary_output = bin(integer)[2:] # removes the 0b used to denote binary with the "bin()" method       
     return binary_output

input_int = 42
print(int_to_binary(input_int))
