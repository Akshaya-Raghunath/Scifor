Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

class Solution(object):
    def moveZeroes(self, nums):
        j=0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                j += 1
    nums=[0,1,0,3,12]
    print(nums)
