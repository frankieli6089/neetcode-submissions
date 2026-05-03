class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_hash_set = set()
            for number in row:
                if number == ".":
                    continue
                elif number in row_hash_set:
                    return False
                else:
                    row_hash_set.add(number)
        
        for col in zip(*board):
            col_hash_set = set()
            for number in col:
                if number == ".":
                    continue
                elif number in col_hash_set:
                    return False
                else:
                    col_hash_set.add(number)

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):

                seen = set()

                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        val = board[r][c]

                        if val == ".":
                            continue

                        if val in seen:
                            return False

                        seen.add(val)
        
        return True


