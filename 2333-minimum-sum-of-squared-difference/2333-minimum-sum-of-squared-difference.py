class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        
        if sum(diffs) <= k:
            return 0
        
        left, right = 0, max(diffs)
        while left < right:
            mid = (left + right) // 2
            ops_needed = sum(max(0, d - mid) for d in diffs)
            
            if ops_needed <= k:
                right = mid
            else:
                left = mid + 1
        
        for i in range(len(diffs)):
            if diffs[i] > left:
                k -= (diffs[i] - left)
                diffs[i] = left
                
        for i in range(len(diffs)):
            if k == 0:
                break
            if diffs[i] == left:
                diffs[i] -= 1
                k -= 1
                
        return sum(d * d for d in diffs)
