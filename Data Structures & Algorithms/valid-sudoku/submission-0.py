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
                val = board[r][c]
                #  accomodating '.'
                if val == ".":
                    continue
                # calculating the indices of values in each sub-sqs
                sq_index = (r // 3) * 3 + (c // 3)

                # checking if the values are present in the hashset for rows, cols and the sub-sqs
                if val in row[r] or val in col[c] or val in sq[sq_index]:
                    return False
                    
                # appending the values tot he set if they not present
                row[r].add(val)
                col[c].add(val)
                sq[sq_index].add(val)

        return True