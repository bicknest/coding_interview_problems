/** Two Sum */

function twoSum(nums, target) {
  if (nums.length < 2) {
    throw "Not enough elements in array for solution";
  }
  const potentialAdditives = new Map();
  for (let idx = 0; idx < nums.length; idx++) {
    if (potentialAdditives.has(nums[idx])) {
      return [idx, potentialAdditives.get(nums[idx])];
    }
    potentialAdditives.set(target - nums[idx], idx);
  }
  throw "No elements found that add to the target";
}

module.exports = twoSum;
