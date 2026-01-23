class Solution(object):
    def removeDuplicates(self, nums):        
        j = 1 
        for i in range(len(nums)):
            if nums[i] != nums[j-1]:
                nums[j],nums[i]=nums[i],nums[j]
                j += 1
        return j
        