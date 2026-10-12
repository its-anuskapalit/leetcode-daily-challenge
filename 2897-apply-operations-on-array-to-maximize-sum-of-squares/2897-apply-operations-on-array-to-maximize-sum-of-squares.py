class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_count = [0] * 31
        for num in nums:
            for bit_position in range(31):
                if num >> bit_position & 1:
                    bit_count[bit_position] += 1
        total_sum = 0
        for _ in range(k):
            current_number = 0
            for bit_position in range(31):
                if bit_count[bit_position] > 0:
                    current_number |= 1 << bit_position
                    bit_count[bit_position] -= 1
            total_sum = (total_sum + current_number * current_number) % MOD
        return total_sum
