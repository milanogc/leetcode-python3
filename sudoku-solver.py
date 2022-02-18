# https://leetcode.com/problems/sudoku-solver

from typing import List

N = 9


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = []
        cols = []
        boxes = []

        for r in range(N):
            rows.append(set())
            cols.append(set())
            boxes.append(set())

        for r in range(N):
            for c in range(N):
                if board[r][c] != ".":
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    box = r // 3 * 3 + c // 3
                    boxes[box].add(val)

        def solveSudokuBacktrack(cell):
            if cell == N * N:
                return True

            r = cell // N
            c = cell - r * N

            if board[r][c] != ".":
                return solveSudokuBacktrack(cell + 1)

            box = r // 3 * 3 + c // 3

            for i in range(1, N + 1):
                val = str(i)

                if val not in rows[r] and val not in cols[c] and val not in boxes[box]:
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box].add(val)

                    if solveSudokuBacktrack(cell + 1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[box].remove(val)

            return False

        solveSudokuBacktrack(0)
        return board


# Tests

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

board_answer = [
    ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
    ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
    ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
    ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
    ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
    ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
    ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
    ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
    ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
]

assert Solution().solveSudoku(board) == board_answer
