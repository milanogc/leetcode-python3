# https://leetcode.com/problems/rotting-oranges

from typing import List
from collections import deque

DIRECTIONS = [
    (-1, 0), # up
    (0, 1), # right
    (1, 0), # down
    (0, -1) # left
]
FRESH_ORANGE = 1
ROTTEN_ORANGE = 2

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        rotten_oranges = deque([])

        for row in range(height):
            for col in range(width):
                if grid[row][col] == ROTTEN_ORANGE:
                    rotten_oranges.append((row, col, 0))

        minutes = 0

        while rotten_oranges:
            row, col, current_minute = rotten_oranges.popleft()
            minutes = max(minutes, current_minute)

            for r, c in DIRECTIONS:
                if 0 <= row + r < height and 0 <= col + c < width and grid[row + r][col + c] == FRESH_ORANGE:
                    grid[row + r][col + c] = ROTTEN_ORANGE
                    rotten_oranges.append((row + r, col + c, current_minute + 1))

        for row in range(height):
            for col in range(width):
                if grid[row][col] == FRESH_ORANGE:
                    return -1

        return minutes

# Tests

assert Solution().orangesRotting([[2]]) == 0
assert Solution().orangesRotting([[2,0]]) == 0
assert Solution().orangesRotting([[0,2]]) == 0
assert Solution().orangesRotting([[0,2,0]]) == 0
assert Solution().orangesRotting([[2,1]]) == 1
assert Solution().orangesRotting([[2,1,0]]) == 1
assert Solution().orangesRotting([[2],[1]]) == 1
assert Solution().orangesRotting([[2,1,1]]) == 2
assert Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
assert Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
assert Solution().orangesRotting([[0,2]]) == 0
assert Solution().orangesRotting([[2,1,1],[1,1,1],[0,1,2]]) == 2