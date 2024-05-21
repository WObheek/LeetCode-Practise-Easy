# Given an integer x, return true if x is a 
# palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:

        #negative number are not palindrome
        if x < 0:
            return False
            
        reversed = 0
        original = x
               
        while x != 0:
            digit = x % 10 # it keeps the remainder : modlus
            reversed = reversed * 10 + digit
            x //= 10 # integer divistion

        return original == reversed



        
