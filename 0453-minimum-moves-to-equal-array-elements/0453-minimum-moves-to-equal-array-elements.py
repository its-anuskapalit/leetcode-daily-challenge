class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_moves= min(nums)
        sum_total= sum(nums)
        return sum_total-min_moves*len(nums)