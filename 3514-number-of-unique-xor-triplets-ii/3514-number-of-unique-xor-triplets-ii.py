class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        max_val = max(nums)
        limit = 1
        while limit <= max_val:
            limit <<= 1
        limit = max(1, limit)
        seen1 = [False] * limit
        for num in nums:
            seen1[num] = True
        seen2 = [False] * limit
        for i in range(limit):
            if seen1[i]:
                for num in nums:
                    seen2[i ^ num] = True
        seen3 = [False] * limit
        for i in range(limit):
            if seen2[i]:
                for num in nums:
                    seen3[i ^ num] = True
        return sum(seen3)
