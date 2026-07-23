/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {

    let ans={}
    for(let elem of strs){
        let temp=(elem.split("").sort()).join("")
        if(!(temp in ans)){
            ans[temp]=[]
        }
        ans[temp].push(elem)

    }
    return Object.values(ans)
};