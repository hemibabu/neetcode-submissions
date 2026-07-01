class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        hashmap = {} # create hashmap for O(1) lookup

        for i in range(len(nums)): # iterate through nums, index based
            j = target - nums[i]
            if j in hashmap and hashmap[j] != i: # if the value j is in haashmap and it is not equal to i
                return [hashmap[j],i] # then return index of j, and i
            else:
                hashmap[nums[i]] = i  # otherwise add the number and store its index. 