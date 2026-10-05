class Solution:

  def longestValidParentheses(self, s: str) -> int:
    n = len(s)
    dp = [0] * (n + 1)
    for i, char in enumerate(s, 1):
      if char == ")":
        if i > 1 and s[i - 2] == "(":
          dp[i] = dp[i - 2] + 2
        else:
          j = i - dp[i - 1] - 1
          if j > 0 and s[j - 1] == "(":
            dp[i] = dp[i - 1] + 2 + dp[j - 1]
    return max(dp)
