class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        # for i in nums, i is the value, not the index
        for i in range(len(nums)): # i is index, j is number, num[i] is number
            j = target - nums[i] # find the complementary number
            if j in hashmap: # check the number if you've seen it
                return [hashmap[j],i]   # if seen, return i and index of j
            else:
                hashmap[nums[i]] = i  # <-- fix what you store