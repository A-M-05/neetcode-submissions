class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for r in range(rows):
            for c in range(cols):
                cell = board[r][c]
                if cell != ".":
                    row_group = r // 3
                    col_group = c // 3
                    b = (row_group * 3) + col_group
                    
                    if cell in row_sets[r]:
                        return False
                    if cell in col_sets[c]:
                        return False
                    if cell in box_sets[b]:
                        return False

                    row_sets[r].add(cell)
                    col_sets[c].add(cell)
                    box_sets[b].add(cell)
        return True
                    