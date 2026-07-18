class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=1
        ans=[]
        for i in range(len(nums)):
            if i!=0:
                left*=nums[i-1]
            ans.append(left)
        right=1
        for j in range(len(nums)-1,-1,-1):
            ans[j]*=right
            right*=nums[j]

        return ans
            

            
        