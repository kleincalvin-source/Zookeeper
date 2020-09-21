""""  Write a code that reads a string from the input, adds 1
to the code point of every character and outputs the
encrypted string """


string = input()
result = ''
for character in string:
    result += chr(ord(character) + 1)

print(result)



