class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        hashmap = {}

        for i in range(len(nums)):
            j = target - nums[i]
            if j in hashmap and hashmap[j] != i:
                return [hashmap[j],i]
            else:
                hashmap[nums[i]] = i