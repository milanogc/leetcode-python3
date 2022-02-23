# https://leetcode.com/problems/n-queens/

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        pos_diags = set()
        neg_diags = set()

        def recursive(row: int):
            if row == n:
                ans.append(["".join(board[i]) for i in range(n)])
                return

            for col in range(n):
                pos_diag = row + col
                neg_diag = row - col

                if (
                    col not in cols
                    and pos_diag not in pos_diags
                    and neg_diag not in neg_diags
                ):
                    board[row][col] = "Q"
                    cols.add(col)
                    pos_diags.add(pos_diag)
                    neg_diags.add(neg_diag)
                    recursive(row + 1)
                    # backtrack
                    board[row][col] = "."
                    cols.remove(col)
                    pos_diags.remove(pos_diag)
                    neg_diags.remove(neg_diag)

        recursive(0)
        return ans


# Tests

assert Solution().solveNQueens(4) == [
    [".Q..", "...Q", "Q...", "..Q."],
    ["..Q.", "Q...", "...Q", ".Q.."],
]
