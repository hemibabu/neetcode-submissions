class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # input; nums = [array of integers]
        # output; len([longest consecutive seq])
        nums_set = set(nums) # converting the array to set for easy O(1) lookup
        seq_len = 0 # create a tracking system for longest seq

        for n in nums_set: # iterate through each elements
            if (n - 1) not in nums_set: # check for previous consecutive value
                length = 1 # establish the first element of the seq
                while (n + length) in nums_set: # create the consecutive seq
                    length += 1
        
                if length > seq_len: # check the length of the sequence with the track system
                    seq_len = length
        return seq_len # return the lenght