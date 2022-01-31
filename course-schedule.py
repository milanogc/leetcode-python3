# https://leetcode.com/problems/course-schedule

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for target, source in prerequisites:
            adj[source].append(target)
            in_degree[target] += 1

        zero_in_degree = []

        for target in range(numCourses):
            if in_degree[target] == 0:
                zero_in_degree.append(target)

        while zero_in_degree:
            source = zero_in_degree.pop()
            numCourses -= 1

            for target in adj[source]:
                in_degree[target] -= 1

                if in_degree[target] == 0:
                    zero_in_degree.append(target)

        return numCourses == 0


# Tests

assert Solution().canFinish(2, [[1, 0]])
assert not Solution().canFinish(2, [[1, 0], [0, 1]])
assert Solution().canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]])
assert Solution().canFinish(6, [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]])
