class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp_closed = [[0] * (k + 1) for _ in range(n + 1)]
        dp_open = [[0] * (k + 1) for _ in range(n + 1)]
        dp_closed[1][0] = 1
        for num_points in range(2, n + 1):
            for num_segments in range(k + 1):
                dp_closed[num_points][num_segments] = (
                    dp_closed[num_points - 1][num_segments] + 
                    dp_open[num_points - 1][num_segments]
                ) % MOD
                dp_open[num_points][num_segments] = dp_open[num_points - 1][num_segments]
              
                if num_segments > 0:
                    dp_open[num_points][num_segments] = (
                        dp_open[num_points][num_segments] +
                        dp_closed[num_points - 1][num_segments - 1] +
                        dp_open[num_points - 1][num_segments - 1]
                    ) % MOD
    
        return (dp_closed[n][k] + dp_open[n][k]) % MOD
