class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # edge case handled 
        
        freq_s = self.freq(s)
        freq_t = self.freq(t)

        return freq_s == freq_t
 
    def freq(self, strs):
        hashy = {}
        for i in strs:
            if i in hashy:
                hashy[i] += 1
            else:
                hashy[i] = 1
        return hashy