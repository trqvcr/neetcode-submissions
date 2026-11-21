# We have to iterate through every cell somehow
# 

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        col_seen = [set() for _ in range(9)]
        grid_seen = [set() for _ in range(9)]
        for row in range(9):
            row_seen = []
            for col in range(9):                # Iterate over the row
                grid_col = col // 3
                grid_row = row // 3
                grid_index = grid_col * 3 + grid_row
                cell = board[row][col]
                if cell == ".":
                    continue
                if cell in row_seen or cell in col_seen[col] or cell in grid_seen[grid_index]:
                    print(cell)
                    return False
                row_seen.append(board[row][col])
                col_seen[col].add(cell)

                grid_seen[grid_index].add(cell)
                print(grid_seen)
        return True