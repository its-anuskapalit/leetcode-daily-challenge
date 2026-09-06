class Solution:

  def numDistinct(self, s: str, t: str) -> int:
    source_len, target_len = len(s), len(t)
    dp = [[0] * (target_len + 1) for _ in range(source_len + 1)]
    for i in range(source_len + 1):
      dp[i][0] = 1
    for i, source_char in enumerate(s, 1):
      for j, target_char in enumerate(t, 1):
        dp[i][j] = dp[i - 1][j]
        if source_char == target_char:
          dp[i][j] += dp[i - 1][j - 1]
    return dp[source_len][target_len]
