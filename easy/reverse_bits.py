# Example 1:
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
# so return 964176192 which its binary representation is 00111001011110000010100101000000.

# Example 2:
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293,
# so return 3221225471 which its binary representation is 10111111111111111111111111111111.


examples = [int('00000010100101000001111010011100', 2), int('11111111111111111111111111111101', 2)]

# print(examples[0].bit_length())

class Solution:
    def __init__(self):
        pass

    @staticmethod
    def reverse_bits(n: int) -> int:
        binary_str = bin(n)[2:]
        binary_str = binary_str.zfill(32)
        reversed_str = binary_str[::-1]
        return int(reversed_str, 2)


solution = Solution
for x_ in examples:
    print(type(bin(x_)[2:]))
    print(solution.reverse_bits(n=x_))


