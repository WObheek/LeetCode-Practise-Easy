/**
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
  - Open brackets must be closed by the same type of brackets.
  - Open brackets must be closed in the correct order.
  - Every close bracket has a corresponding open bracket of the same type.
**/

class Solution:
    def isValid(self, s: str) -> bool:

        # paired: opening & closing parenthesis
        brackets={
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        # initializing empty stack
        stack=[]
        
        # looping through given string
        for bracket in s:

            # if the bracket belongs to opening
            if bracket in brackets.keys():
                stack.append(bracket)
            
            # if the bracket belong to closing parenthesis & stack is not empty
            elif bracket in brackets.values():
                
                #if stack is empty returns false
                if not stack:
                    return False
                # taking out the last element of stack if not empty else return false
                last_paren = stack.pop() 
                
                # comparing last parenthesis
                if brackets[last_paren] != bracket:
                    return False
                

        # returns true if stack is empty & returns fasl if stack in not empty
        return not stack


/**
# Example usage:
solution = Solution()
print(solution.isValid("()"))      # True
print(solution.isValid("()[]{}"))  # True
print(solution.isValid("(]"))      # False
print(solution.isValid("([)]"))    # False
print(solution.isValid("{[]}"))    # True

**/


            


                    
            


                
                
                
        

        

        
