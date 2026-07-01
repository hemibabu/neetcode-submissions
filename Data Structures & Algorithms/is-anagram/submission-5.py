class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # create a hash map/ frequency map of string s and t
        # check the lenght of the strings
        if len(s) != len(t): #anagrams are equal in lenght
            return False

        # create an empty dict
        freq_s,freq_t = {},{}


        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1

        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1


        # comparison of dicts
        if freq_s == freq_t:
            return True
        else:
            return False