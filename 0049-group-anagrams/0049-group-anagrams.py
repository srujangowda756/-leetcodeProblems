class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dec={}
        for item in strs:
            item.replace(" ","")
            key=''.join(sorted(item))
            print(key)
            if key in dec:
                dec[key].append(item)
            else:
                dec[key]=[item]
        res=[]
        for j in dec.values():
            res.append(j)
        res.sort(key=len)
        return res
        

        