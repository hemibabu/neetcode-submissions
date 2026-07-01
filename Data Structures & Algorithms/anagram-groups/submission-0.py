class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input; array of strings---> strs = ["","",..]
        # output; group of anagrams as substrings ---> [["","",...], ["","",...]]

        # hashmap for O(1) lookup since its just one array as input
        hashmap = {}

# create a function to create frequency map for each string in the array
# loop through the strs using the built function to create frequency map of each strings as nested dict

# while that is going on, using O(1) lookup we check if the string has same frequency map
# as one and store that with the frequency map in the same dict
# and then we return the strings that are paired with same frequency map as sublists.

# function to create frequency map for each string
        def create_freq_map(s): # helper function
            count = [0] * 26 # edge case- lower case alphabets
            for char in s:
                count[ord(char) - ord('a')] += 1 
        # print(count) # prints list of count
        # access the array location by count[of the letter in a string], 
        # and then convert s[chars] to ASCII using ord()
            return tuple(count)  # tuple so it can be used as a dict key

# loop through strs, create frequency map, use O(1) lookup to group
        for word in strs:
            key = create_freq_map(word)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)
    
# return the strings paired with same frequency map as sublists
        return list(hashmap.values())