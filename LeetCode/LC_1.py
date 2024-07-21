#Om Namah Shivaya
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        i =0
        j = len(nums)-1
        while(i<len(nums)-1 and j>=0):
            if(nums[i]+nums[j]==target):
                res.append(i)
                res.append(j)
                break
            elif (nums[i]+nums[j]<target):
                i+=1
            elif(nums[i]+nums[j]>target):
                j-=1
        return res