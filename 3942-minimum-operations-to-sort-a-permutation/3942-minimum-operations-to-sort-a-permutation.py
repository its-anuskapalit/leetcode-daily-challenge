class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        zero = nums.index(0)
        is_right_inc = True
        for i in range(n):
            if nums[(zero + i) % n] != i:
                is_right_inc = False
                break
                
        is_left_inc = True
        for i in range(n):
            if nums[(zero - i) % n] != i:
                is_left_inc = False
                break
                
        ans = float('inf')
        
        if is_right_inc:
            ops_a = zero
            ops_b = 2 + (n - zero)
            ans = min(ans, ops_a, ops_b)
            
        if is_left_inc:
            ops_c = (zero + 1) + 1
            ops_d = 1 + (n - zero - 1)
            ans = min(ans, ops_c, ops_d)
            
        return ans if ans != float('inf') else -1
