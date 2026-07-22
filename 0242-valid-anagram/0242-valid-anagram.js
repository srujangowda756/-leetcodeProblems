/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(s.length!==t.length){
        return false
    }
    let freq1 = new Array(26).fill(0)
    let freq2 = new Array(26).fill(0)
    for(let i of s){
        idx = i.charCodeAt(0)-"a".charCodeAt(0)
        freq1[idx]++
    }
    for(let i of t){
        idx = i.charCodeAt(0)-"a".charCodeAt(0)
        freq2[idx]++
    }     
    return freq1.join("")===freq2.join("")
};