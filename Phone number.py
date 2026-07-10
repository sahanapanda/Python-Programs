class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Edge case: if the input is empty, return an empty list
        if not digits:
            return []
            
        # Mapping of digits to letters matching a standard phone keypad
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        combinations = []
        
        def backtrack(index, path):
            # If the current path length equals digits length, a full combination is formed
            if len(path) == len(digits):
                combinations.append("".join(path))
                return
            
            # Get the letters that the current digit maps to
            current_digit = digits[index]
            letters = phone_map[current_digit]
            
            # Explore each letter for the current digit
            for letter in letters:
                path.append(letter)          # Choose the letter
                backtrack(index + 1, path)   # Move to the next digit
                path.pop()                   # Backtrack and try the next letter
                
        # Start the backtracking process from the 0-th index with an empty path
        backtrack(0, [])
        return combinations
