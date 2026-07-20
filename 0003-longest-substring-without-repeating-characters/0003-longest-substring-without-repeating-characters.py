class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        left=0
        stack=set()

        for i in range(len(s)):
            while s[i] in stack:
                stack.remove(s[left])
                left+=1
            stack.add(s[i])
            ans=max(ans,i-left+1)
        return ans

        