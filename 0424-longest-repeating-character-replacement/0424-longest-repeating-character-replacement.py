class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        ans=0
        max_freq=0
        stack={}

        for right in range(len(s)):
            stack[s[right]]=stack.get(s[right],0)+1
            max_freq = max(max_freq,stack[s[right]])

            while (right-left+1)-max_freq>k:
                stack[s[left]]-=1
                left+=1
    
            ans=max(ans,right-left+1)
        return ans
            
        