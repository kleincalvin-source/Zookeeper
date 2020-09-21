# coded message
coded_message = str(input())


# key integer number
key_number = int(input())

# convert key to 2 bites and sum it up
key_number_to_two_bytes = sum(key_number.to_bytes(2, byteorder='little'))

print(''.join([chr(ord(c) + key_number_to_two_bytes) for c in coded_message]))
