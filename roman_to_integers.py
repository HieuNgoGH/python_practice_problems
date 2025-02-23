"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer."""

def romanToInt(self, s: str) -> int:
    integer = 0
    roman_int_array = []

    for item in s:
        if item == 'I':
            roman_int_array.append(1)
        elif item == 'V':
            roman_int_array.append(5)
        elif item == 'X':
            roman_int_array.append(10)
        elif item == 'L':
            roman_int_array.append(50)
        elif item == 'C':
            roman_int_array.append(100)
        elif item == 'D':
            roman_int_array.append(500)
        elif item == 'M':
            roman_int_array.append(1000)

    counter = len(roman_int_array) - 1
    counter2 = counter - 1
    integer = integer + roman_int_array[counter]
    while counter2 >= 0:
        if roman_int_array[counter2] > roman_int_array[counter]:
            integer = integer + roman_int_array[counter2]
            counter -= 1
            counter2 -= 1
        else:
            integer = integer - roman_int_array[counter2]
            counter -= 1
            counter2 -= 1

    return integer


#a = Solution()
#string = "VI"
#print(a.romanToInt(string))

