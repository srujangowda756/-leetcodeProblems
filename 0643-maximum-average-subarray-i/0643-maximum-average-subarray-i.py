class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans=sum(nums[:k])
        window=ans
        n=len(nums)
        for i in range(k,n):
            window+=nums[i]-nums[i-k]
            ans=max(ans,window)
        return ans/k
        