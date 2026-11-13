class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_length = 1
        current_length = 1

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 1

        current_length = 1

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 1

        return max_length
