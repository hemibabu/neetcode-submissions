class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def freq_map(s):
            count = [0]*26
            for char in s:
                count[ord(char) - ord('a')] += 1
            return tuple(count)

        hashmap = {}

        for word in strs:
            key = freq_map(word)
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]
        
        return list(hashmap.values())


