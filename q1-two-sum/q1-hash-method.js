// LeetCode 1.
// https://leetcode.com/problems/two-sum/

const twoSum = function(nums, target) {
    const ans = [];
    const mapping = new Map() // store {value: position}

    for (let i = 0; i< nums.length; i++) {
        let com = target - nums[i];

        if (mapping.has(nums[i])) {
            return [mapping.get(nums[i]), i];
        }

        mapping.set(com, i);
    }
}

// time: O(n)
// space: O(n)