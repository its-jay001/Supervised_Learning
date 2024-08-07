def reverse_string(input_str):
    reversed_str = ''
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str

input_string = "hello"
reversed_string = reverse_string(input_string)
print(reversed_string)
