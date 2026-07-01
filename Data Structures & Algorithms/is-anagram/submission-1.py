class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # create a hash map/ frequency map of string s and t
        # create an empty dict
        freq_s = {}
        # frequency map of s
        for char in s:
            if char in freq_s:
                freq_s[char] += 1  #adding count to each character
            else:
                freq_s[char] = 1 #creatinga the count for new characters

        # null dict for t      
        freq_t = {}
        # fdrequency map of t
        for char in t:
            if char in freq_t:
                freq_t[char] += 1
            else:
                freq_t[char] = 1

        if freq_s == freq_t:
            return True
        else:
            return False