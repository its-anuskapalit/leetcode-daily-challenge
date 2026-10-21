class Solution:
  def targetIndices(self, nums: list[int], target: int) -> list[int]:
    nums.sort()
    return [index for index, num in enumerate(nums) if num==target]