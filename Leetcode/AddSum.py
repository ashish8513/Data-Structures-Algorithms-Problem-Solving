class Solution(object):
    def twoSum(self, nums, target):
        
        nums_dict = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_dict:
                return [nums_dict[diff], i]
            else:
                nums_dict[nums[i]] = i


nms = [3,2,4]

targ = 6
print(Solution().twoSum(nms, target=targ))