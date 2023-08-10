# Write a function that takes a bytes object as input and decodes it to a string using UTF-8 encoding.

#uses the built in function decode()

""" Example:
Input: b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
Output: "Hello, 世界"
 """


def decode_to_string(input_bytes)-> str:
    string = input_bytes.decode("utf-8")
    return string



# Test the function
input_bytes = b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
print(decode_to_string(input_bytes))