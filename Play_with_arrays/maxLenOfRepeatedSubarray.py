'''
leetcode
718. Maximum Length of Repeated Subarray
https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/

'''

from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        index1, len1, len2, maxLen = 0, len(nums1), len(nums2), 0
        while index1 < len1:
            index2 = 0
            while index2 < len2:
                actMaxLen = 0
                while index1 + actMaxLen < len1 and index2 + actMaxLen < len2 and nums1[index1 + actMaxLen] == nums2[index2 + actMaxLen]:
                    actMaxLen += 1
                maxLen = max(maxLen, actMaxLen)
                index2 += 1
                if maxLen >= len2 - index2:
                    break
            index1 += 1
            if maxLen >= len1 - index1:
                break
        return maxLen
    
    # quicker solution
    def findLengthDynamic(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        tableDynamic = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    tableDynamic[i + 1][j + 1] = tableDynamic[i][j] + 1

        return max(map(max, tableDynamic))


def main():
    # tests
    sol = Solution()
    # test 1
    nums1 = [1,2,3,2,1]
    nums2 = [3,2,1,4,7]
    print(sol.findLength(nums1, nums2), 'should equal 3')
    print(sol.findLengthDynamic(nums1, nums2), 'should equal 3')
    # test 2
    nums1 = [0,0,0,0,0]
    nums2 = [0,0,0,0,0]
    print(sol.findLength(nums1, nums2), 'should equal 5')
    print(sol.findLengthDynamic(nums1, nums2), 'should equal 5')
    # test 3
    nums1 = [0,0,0,0,0,0,1,0,0,0]
    nums2 = [0,0,0,0,0,0,0,1,0,0]
    print(sol.findLength(nums1, nums2), 'should equal 9')
    print(sol.findLengthDynamic(nums1, nums2), 'should equal 9')

if __name__ == '__main__':
    main()





