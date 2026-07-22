/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hash={}
    for(let i=0;i<nums.length;i++){
        let temp=target-nums[i]
        if(temp in hash){
            return [hash[temp],i]
        }
        hash[nums[i]]=i
    }    
};