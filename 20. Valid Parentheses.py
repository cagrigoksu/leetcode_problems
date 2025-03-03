class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        sym = {
            '{': 1, '}': -1,
            '[': 2, ']': -2,
            '(': 3, ')': -3
            }
        
        isValid = True
        
        temp = []
        
        for char in s:
            
            # char is any of paranthesis 
            if char in sym.keys() or char in sym.values():
                
                if len(temp) == 0 and sym[char] > 0:   # first parentheses must be openings
                    temp.append(sym[char])
                elif len(temp) == 0 and sym[char] < 0:   # first parentheses cannot be closings
                    isValid = False
                    break
                elif len(temp) > 0 and sym[char] > 0:   # allow nested parentheses
                    temp.append(sym[char])
                elif len(temp) > 0 and sym[char] < 0:   # remove the last parentheses pair in nest
                    if temp[-1] == sym[char] * -1:
                        temp.pop()
                    else:
                        isValid = False
                        break                
        
        return isValid
                    
                
    
                
print(Solution().isValid('()')) # valid
print(Solution().isValid('()[]/{/}'))   # valid
print(Solution().isValid('(]')) # invalid
print(Solution().isValid('([])'))   # valid
        
""" EASY
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""