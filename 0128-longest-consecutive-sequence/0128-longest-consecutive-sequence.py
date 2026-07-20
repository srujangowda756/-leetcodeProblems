class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums=set(nums)
        ans=0
        for i in set_nums:
            if i-1 in set_nums:
                continue
            count=1
            cur=i+1
            for j in range(len(set_nums)):
                if cur in set_nums:
                    count+=1
                    cur+=1
                else:
                    break
            ans=max(ans,count)
        return ans


            
        