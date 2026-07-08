class Solution:
    def secondHighest(self, s: str) -> int:
        fir=-1
        sec=-1
        for i in s:
            if i.isdigit():
                num=int(i)
                if num>fir:
                    sec=fir
                    fir=num
                elif num>sec and num!=fir:
                    sec=num
        return sec