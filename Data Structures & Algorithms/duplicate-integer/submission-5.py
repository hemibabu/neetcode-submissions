class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

 
 
 # input = nums array
 # check for repetition of a value inside the array, then return true

 # hash set works fine for O1 lookups since it is just one array checking against itself

        hashset = set()

        for values in nums:
            if values in hashset:
                return True
            hashset.add(values)
        return False