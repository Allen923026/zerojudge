def roman_to_int(roman):
    dict_roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    result = 0
    pre_value = 0
    for char in reversed(roman):
        value = dict_roman[char]
        if value < pre_value:
            result -= value
        else:
            result +=value
        
        pre_value = value
    return result

def int_to_roman(num):
    result = ""
    for value,numeral in (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),('C', 100), ('XC', 90), 
                          ('L', 50), ('XL', 40),('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)):
        count = num//numeral
        result += count*value
        num -= count*numeral
    return result

while True:
    try:
        r1,r2 = input().split()
        result = abs(roman_to_int(r1)-roman_to_int(r2))
        output = int_to_roman(result)
        if result == 0:
            print("ZERO")
        else:
            print(output)
    except:
        break