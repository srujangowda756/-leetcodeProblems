/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let left=0
    let right=s.length-1

    const isApha=c=> /[a-zA-Z0-9]/i.test(c)

    while(left<right){
        while(left<right && !isApha(s[left])){
            left++
        }
        while(left<right && !isApha(s[right])){
            right--
        }
        if(s[right].toLowerCase()!==s[left].toLowerCase()){
            return false
        }
        left++
        right--
    }   
    return true 
};