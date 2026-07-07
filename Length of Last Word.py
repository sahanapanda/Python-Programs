class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # split() without arguments automatically strips padding 
        # and splits by any consecutive whitespace.
        words = s.split()
        
        if not words:
            return 0
            
        return len(words[-1])
