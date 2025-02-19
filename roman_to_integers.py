#

class Solution:
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


a = Solution()
string = "VI"
print(a.romanToInt(string))

