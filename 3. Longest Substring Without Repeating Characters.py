class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = []
        window_temp = []

        if len(s) == 1:
            return 0 if s[0]=='' else 1  
        elif len(s) > 1 :
            for idx, char in enumerate(s):
                if char not in window:
                    window.append(char) 
                else:
                    w_idx = window.index(char)
                    window_temp.append(window)
                    window = window[w_idx+1:]
                    window.append(char) 

        window_temp.append(window)        
        result = len(max(window_temp, key=len)) if len(window_temp) > 0 else 0
        return result

""" MEDIUM
Given a string s, find the length of the longest substring without duplicate characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""