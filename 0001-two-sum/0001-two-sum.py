class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            first=target-nums[i]
            if first in d:
                return [d[first],i]      
            d[nums[i]]=i

