# https://leetcode.com/problems/time-needed-to-inform-all-employees

from typing import List

class Solution:
    def numOfMinutes(self, n: int, head_id: int, managers: List[int], inform_time: List[int]) -> int:
        connections = [[] for _ in range(n)]

        for employee_id, manager_id in enumerate(managers):
            if employee_id != head_id:
                connections[manager_id].append(employee_id)

        return self._calculateMinutes(head_id, connections, inform_time) # depth-first search

    def _calculateMinutes(self, manager_id: int, connections: List[List[int]], inform_time: List[int]) -> int:
        max_minutes = 0

        for employee_id in connections[manager_id]:
            max_minutes = max(max_minutes, self._calculateMinutes(employee_id, connections, inform_time))

        return inform_time[manager_id] + max_minutes

# Tests

assert Solution().numOfMinutes(1, 0, [-1], [0]) == 0
assert Solution().numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]) == 1
assert Solution().numOfMinutes(8, 4, [2,2,4,6,-1,4,4,5], [0,0,4,0,7,3,6,0]) == 13
