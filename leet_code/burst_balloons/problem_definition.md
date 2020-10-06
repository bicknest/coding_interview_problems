## Burst Balloons

Given n balloons, indexed from 0 to n -1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons.
If you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indicies of i. After the burst, left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

- you may imagine nums[-1] = nums[n] = 1. They are not real, therefore you cannot burst them

- 0 <= nums[i] <= 100 (the balloon number has to be positive)
