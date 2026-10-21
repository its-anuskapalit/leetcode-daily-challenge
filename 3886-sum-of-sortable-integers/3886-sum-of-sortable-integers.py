class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
       
        def check(k: int) -> bool:
            prev_max = float('-inf')
            
            for i in range(0, n, k):
                block = nums[i : i + k]
                
                descents = 0
                for j in range(k):
                    if block[j] > block[(j + 1) % k]:
                        descents += 1
                        
                if descents > 1:
                    return False
    
                if descents == 0:
                    curr_min = block[0]
                    curr_max = block[-1]
                else:
                    
                    drop_idx = -1
                    for j in range(k):
                        if block[j] > block[(j + 1) % k]:
                            drop_idx = j
                            break
                    
                    curr_min = block[(drop_idx + 1) % k]
                    curr_max = block[drop_idx]
                
                if curr_min < prev_max:
                    return False
                
                prev_max = curr_max
                
            return True

        for k in range(1, n + 1):
            if n % k == 0:
                if check(k):
                    ans += k
                    
        return ans
