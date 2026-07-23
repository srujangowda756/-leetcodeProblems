/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let ans=nums[0]
    let tot=0
    for(let i=0;i<nums.length;i++){
        tot+=nums[i]
        if(tot>ans){
            ans=tot
        }
        if(tot<0){
            tot=0
        }
    }
    return ans
    
};