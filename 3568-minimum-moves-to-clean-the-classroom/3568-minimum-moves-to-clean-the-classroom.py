class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
    
        rows, cols = len(classroom), len(classroom[0])
      
        lamp_indices = [[0] * cols for _ in range(rows)]
      
        start_row = start_col = lamp_count = 0
        for row_idx, row in enumerate(classroom):
            for col_idx, cell in enumerate(row):
                if cell == "S":
                    start_row, start_col = row_idx, col_idx
                elif cell == "L":
                    lamp_indices[row_idx][col_idx] = lamp_count
                    lamp_count += 1
      
        if lamp_count == 0:
            return 0
      
        visited = [
            [[[False] * (1 << lamp_count) for _ in range(energy + 1)] for _ in range(cols)]
            for _ in range(rows)
        ]
        queue = [(start_row, start_col, energy, (1 << lamp_count) - 1)]
        visited[start_row][start_col][energy][(1 << lamp_count) - 1] = True
      
        directions = (-1, 0, 1, 0, -1)
    
        moves = 0
      
        while queue:
            current_level = queue
            queue = []
          
            for current_row, current_col, current_energy, lamp_mask in current_level:
                if lamp_mask == 0:
                    return moves
              
                if current_energy <= 0:
                    continue
                for direction_idx in range(4):
                    next_row = current_row + directions[direction_idx]
                    next_col = current_col + directions[direction_idx + 1]
                    if 0 <= next_row < rows and 0 <= next_col < cols and classroom[next_row][next_col] != "X":
                        next_energy = (
                            energy if classroom[next_row][next_col] == "R" else current_energy - 1
                        )
                      
                        next_lamp_mask = lamp_mask
                        if classroom[next_row][next_col] == "L":
                            next_lamp_mask &= ~(1 << lamp_indices[next_row][next_col])
                        if not visited[next_row][next_col][next_energy][next_lamp_mask]:
                            visited[next_row][next_col][next_energy][next_lamp_mask] = True
                            queue.append((next_row, next_col, next_energy, next_lamp_mask))
    
            moves += 1
        return -1
