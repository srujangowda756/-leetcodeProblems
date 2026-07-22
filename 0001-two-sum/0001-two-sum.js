/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let stack={}
    for(let i=0;i<nums.length;i++){
        temp=target-nums[i]
        if(temp in stack){
            return [stack[temp],i]
        }
        stack[nums[i]]=i
    }    
};