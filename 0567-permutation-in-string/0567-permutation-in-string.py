from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        length=len(s1)
        s1_count=Counter(s1)

        for i in range(len(s2)-length+1):
                   
            if s1_count==Counter(s2[i:i+length]): 
                return True
        return False
        