# convert given string to a bytes
given_string = str(input())
given_string_to_bytes = given_string.encode()

# output the last item
print(given_string_to_bytes[-1])
