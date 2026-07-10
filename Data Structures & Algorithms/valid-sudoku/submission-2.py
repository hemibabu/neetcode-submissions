class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # input; board = array of lists
        # output; true/false
        # initialize three hashsets for O(1) lookups
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sq = [set() for _ in range(9)]

        # iterate through the loop to access each values
        for r in range(9):
            for c in range(9):
                #  accomodating '.'
                if board[r][c] == ".":
                    continue
                # calculating the indices of values in each sub-sqs
                sq_index = (r // 3) * 3 + (c // 3)

                # checking if the values are present in the hashset for rows, cols and the sub-sqs
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in sq[sq_index]:
                    return False

                # appending the values tot he set if they not present
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                sq[sq_index].add(board[r][c])

        return True