from collections import deque
from typing import List


def checkIfItHasOverlappingPart(top: List[int], new: List[int]) -> bool:
    return top[1] >= new[0]


class Solution:
   
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        stack = deque()
        index = 0
        while index <= len(intervals) - 1:
            if len(stack) == 0:
                stack.append(intervals[index])
            elif checkIfItHasOverlappingPart(stack[-1], intervals[index]):
                top = stack[-1]
                new = intervals[index]
                stack.pop()
                stack.append([top[0], max(new[1], top[1])])
            else:
                stack.append(intervals[index])
            index += 1

        return list(stack)