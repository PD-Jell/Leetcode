class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for indexI in range(0, len(nums)):
            i = nums[indexI]
            targetX = target - i
            if targetX in nums:
                if indexI != nums.index(targetX):
                    return [indexI, nums.index(targetX)]