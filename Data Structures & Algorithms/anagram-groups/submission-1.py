class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # helper function
        def create_freq_map(s):
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            return tuple(count)
        # frequency map for each word created to be stored as tuple key

        result = {} # hashmap for the results
        for word in strs: # loop through the words in the string to create freq map of the array of strings
            key = create_freq_map(word)
            if key in result:
                result[key].append(word)
            else:
                result[key] = [word]

        return list(result.values())