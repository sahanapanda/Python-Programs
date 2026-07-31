class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            
            # Calculate the sum of the squares of its digits
            total_sum = 0
            while n > 0:
                digit = n % 10
                total_sum += digit ** 2
                n //= 10
                
            n = total_sum
            
        return n == 1
