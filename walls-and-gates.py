# https://leetcode.com/problems/walls-and-gates

from typing import List
from collections import deque

DIRECTIONS = [
    (-1, 0), # up
    (0, 1), # right
    (1, 0), # down
    (0, -1) # left
]
GATE = 0
INF = 2147483647

class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> List[List[int]]:
        height = len(grid)
        width = len(grid[0])

        for i in range(height):
            for j in range(width):
                if grid[i][j] == GATE:
                    queue = deque([(i, j)])
                    elements_per_level = 1
                    distance = 1

                    while queue:
                        if elements_per_level == 0:
                            distance += 1
                            elements_per_level = len(queue)

                        row, col = queue.popleft()
                        elements_per_level -= 1

                        for r, c in DIRECTIONS:
                            if 0 <= row + r < height and 0 <= col + c < width and grid[row + r][col + c] > distance:
                                grid[row + r][col + c] = distance
                                queue.append((row + r, col + c))

        return grid

# Tests

assert Solution().wallsAndGates([
    [INF,  -1,  0,  INF],
    [INF, INF, INF,  -1],
    [INF,  -1, INF,  -1],
    [0,  -1, INF, INF]
]) == [
    [3, -1, 0, 1],
    [2, 2, 1, -1],
    [1, -1, 2, -1],
    [0, -1, 3, 4]
]
