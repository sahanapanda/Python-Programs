class Solution(object):
    def reverseBits(self, n):
        result = 0
        for _ in range(32):
            # Shift result left to make room for the next bit
            result = (result << 1) | (n & 1)
            # Shift n right to process the next bit
            n >>= 1
        return result
