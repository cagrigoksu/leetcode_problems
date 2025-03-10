class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        shortest_str = min(strs, key=len)
        strs.remove(shortest_str)
        
        for st in strs:
            
            while not st.startswith(shortest_str):
                
                shortest_str = shortest_str[:-1]
                
                if not shortest_str:
                    return ""
                
        return shortest_str
        
s = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(s)) 

""" EASY
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""       