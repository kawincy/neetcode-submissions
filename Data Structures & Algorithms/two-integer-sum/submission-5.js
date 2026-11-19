class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let hashMap = new Map();
        for(let idx in nums) {
            if (hashMap.has(target - nums[idx])) {
                // console.log(hashMap)
                return [Number(idx), Number(hashMap.get(target - nums[idx]))];
            }
            hashMap.set(nums[idx], idx);
        }
    }
}
