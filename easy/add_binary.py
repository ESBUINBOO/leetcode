# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

examples = [["11", "1"], ["1010", "1011"]]


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def add_binary(a: str, b: str) -> str:
        sum = bin(int(a, 2) + int(b, 2))
        return sum[2:]


solution = Solution()
for i in examples:
    print(solution.add_binary(a=i[0], b=i[1]))
