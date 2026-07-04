class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # List of tuples containing (value, roman_symbol) sorted in descending order
        roman_mapping = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = []
        
        for value, symbol in roman_mapping:
            # If num is 0, we can stop early
            if num == 0:
                break
                
            # Determine how many times this symbol fits into num
            count = num // value
            if count:
                result.append(symbol * count)
                num %= value  # Update num to the remainder
                
        return "".join(result)
