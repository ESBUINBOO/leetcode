from typing import List

# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

# NUMS = [2, 7, 11, 15]
# TARGET = 9
# NUMS = [3,2,4]
# TARGET = 6

NUMS = [3, 0, 3]
TARGET = 6


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def two_sum(nums: List, target: int) -> List:
        # Create a hash table to store the value and its index
        hash_table = {}
        for i in range(len(nums)):
            # Check if the difference between the target and the current element is in the hash table
            diff = target - nums[i]
            if diff in hash_table:
                # If it is, we have found the two numbers that add up to the target
                return [hash_table[diff], i]
            # If the difference is not in the hash table, add the current element and its index to the hash table
            hash_table[nums[i]] = i
        # If no solution is found, return an empty list
        return []


solution = Solution
print(solution.two_sum(nums=NUMS, target=TARGET))


