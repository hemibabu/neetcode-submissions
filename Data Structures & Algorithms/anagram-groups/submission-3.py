class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create helper function for the words
        def freq_map(s):
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            return tuple(count)
        
        # freq map for the array of strings
        # init an empty dict
        hashmap = {}
        for word in strs:
            key = freq_map(word)
            #append the tuple keys into the dict
            if key in hashmap:
                hashmap[key].append(word)

            else:
                hashmap[key] = [word]
        return list(hashmap.values())