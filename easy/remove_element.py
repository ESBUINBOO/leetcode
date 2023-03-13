# Example 1:
#
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:
#
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

from typing import List

examples = [{"nums": [3, 2, 2, 3], "val": 3},
            {"nums": [0, 1, 2, 2, 3, 0, 4, 2], "val": 2}]


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def remove_element(nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


solution = Solution()
for _nums in examples:
    print(solution.remove_element(nums=_nums["nums"], val=_nums["val"]))