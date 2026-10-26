class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            
            total = grid[r][c]
            grid[r][c] = 0
            
            total += dfs(r + 1, c)
            total += dfs(r - 1, c)
            total += dfs(r, c + 1)
            total += dfs(r, c - 1)
            
            return total

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    island_value = dfs(i, j)
                    if island_value % k == 0:
                        island_count += 1
                        
        return island_count
