# You are given an integer array 
# n
# u
# m
# s
# nums. Rotate the array to the right by 
# k
# k positions, where 
# k
# k is a non-negative integer.
# For example:
# Given the array [10, 20, 30, 40, 50], rotating it two times to the right results in:
# First rotation - [50, 10, 20, 30, 40]
# Second rotation - [40, 50, 10, 20, 30]
# You need to implement a solution that operates in-place and uses only 
# O
# (
# 1
# )
# O(1) additional space.
# You don’t need to print any values; simply edit the values of the array.

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n 

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)

        reverse(0, k - 1)

        reverse(k, n - 1)
