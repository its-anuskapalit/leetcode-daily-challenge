class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        array_length = len(nums)
        for start_index in range(array_length):
            distinct_elements = set()
            for end_index in range(start_index, array_length):
                distinct_elements.add(nums[end_index])
                distinct_count = len(distinct_elements)
                total_sum += distinct_count * distinct_count
        return total_sum
