data = input()

for i in data:
    ascii_code = ord(i)
    ascii_code -= 7
    letter = chr(ascii_code)
    print(letter,end='')