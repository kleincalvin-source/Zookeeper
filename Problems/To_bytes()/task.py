# write code that takes a given number

given_number = int(input())

# converts it to a byte object

bytes_given_number = given_number.to_bytes(2, byteorder='little')
# print(bytes_given_number)
# print(bytes_given_number)
# convert to integers
print(sum(bytes_given_number))


# bytes_given_number_to_int = int.from_bytes(bytes_given_number, 'little')

# print(bytes_given_number_to_int)

