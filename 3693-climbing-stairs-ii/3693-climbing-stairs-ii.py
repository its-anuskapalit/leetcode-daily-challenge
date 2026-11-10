class Solution:
  def climbStairs(self, n: int, costs: List[int]) -> int:
    n = len(costs)
    inf = float('inf')
    f = [inf] * (n + 1)
    f[0] = 0
    for i, x in enumerate(costs, 1):
      for j in range(max(0, i - 3), i):
        f[i] = min(f[i], f[j] + x + (i - j) ** 2)
    return f[n]
