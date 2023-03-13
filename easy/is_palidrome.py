# Example 1:
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

examples = [121, -121, 10, 123454321, 113111]


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def is_palidrome(x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]


solution = Solution
for x_ in examples:
    print(solution.is_palidrome(x=x_))


