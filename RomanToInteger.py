class Solution:
    def romanToInt(self, s: str) -> int:

        roman_int= {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        result = 0
        index = 0

        while index < len(s):
           
            # Checks If the current value is less than the next value, subtract the current value : eg: IX, IV
            # Checks if The index is not the last index 
            if index + 1 < len(s) and roman_int[s[index]] < roman_int[s[index+1]]:
                result += roman_int[s[index+1]] - roman_int[s[index]]
                index += 2
            else:
                result += roman_int[s[index]]
                index +=1

        return result


# Example usage
# solution = Solution()
# print(solution.romanToInt("IX"))  # Output should be 9
# print(solution.romanToInt("LVIII"))  # Output should be 58
# print(solution.romanToInt("MCMXCIV"))  # Output should be 1994
