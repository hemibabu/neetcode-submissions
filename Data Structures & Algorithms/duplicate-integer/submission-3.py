class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # understand 
        # find if theres a dup in the list 
        # expected return: bopolean 

        # code 
        # init dict 
        seen = set()

        # loop through 
        for number in nums:
            if number in seen:
                return True
            else:
                seen.add(number)

        return False 
        