/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let left=0
    let ans=0
    let set = new Set()
    for(let i=0;i<s.length;i++){
        while(set.has(s[i])){
            set.delete(s[left])
            left++
        }
        set.add(s[i])
        if (ans<(i-left+1)){
            ans=i-left+1
        }
    }     
    return ans
};