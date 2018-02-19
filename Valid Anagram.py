class Solution(object):
    from collections import Counter
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """      
        if len(s) != len(t):
            return False
            
            
        else:                
            return Counter(s).items() == Counter(t).items()
        
