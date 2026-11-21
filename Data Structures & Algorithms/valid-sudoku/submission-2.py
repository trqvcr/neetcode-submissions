# We have to iterate through every cell somehow
# 

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        col_seen = [set() for _ in range(9)]
        grid_seen = [set() for _ in range(9)]
        for row in range(9):
            row_seen = set()
            for col in range(9):                # Iterate over the row
                cell = board[row][col]

                if cell == ".":
                    continue
                grid_col = col // 3
                grid_row = row // 3
                grid_index = grid_col * 3 + grid_row
                
                if cell in row_seen or cell in col_seen[col] or cell in grid_seen[grid_index]:
                    return False
                row_seen.add(board[row][col])
                col_seen[col].add(cell)

                grid_seen[grid_index].add(cell)
        return True