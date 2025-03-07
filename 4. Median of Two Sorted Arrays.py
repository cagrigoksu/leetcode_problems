import math

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        nums1 = nums1 + nums2
        nums1.sort()

        listCount = len(nums1)

        if listCount == 1:
            return nums1[0]

        if listCount >= 2 and listCount % 2 == 0:
            return float( nums1[(listCount/2)-1] + nums1[listCount/2] ) / 2

        if listCount >= 2 and listCount % 2 == 1:  
            idx = int(math.ceil(float(listCount)/2))
            return (nums1[idx-1])
        
""" HARD
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""