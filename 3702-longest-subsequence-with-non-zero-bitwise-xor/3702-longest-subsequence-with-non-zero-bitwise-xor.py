class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n=len(nums)
        if all(x==0 for x in nums):
            return 0
        total= functools.reduce(lambda x,y:x^y,nums,0)
        if total!=0:
            return n
        else:
            return n-1