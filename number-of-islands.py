# https://leetcode.com/problems/number-of-islands

from typing import List
from collections import deque

DIRECTIONS = [
    (-1, 0), # up
    (0, 1), # right
    (1, 0), # down
    (0, -1) # left
]
WATER = "0"
LAND = "1"

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        islands = 0

        for start_row in range(height):
            for start_col in range(width):
                if grid[start_row][start_col] == LAND:
                    islands += 1
                    queue = deque([(start_row, start_col)])

                    while queue:
                        row, col = queue.popleft()

                        if 0 <= row < height and 0 <= col < width and grid[row][col] == LAND:
                            grid[row][col] = WATER

                            for r, c in DIRECTIONS:
                                queue.append((row + r, col + c))

        return islands

# Tests

assert Solution().numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]) == 1

assert Solution().numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]) == 3
