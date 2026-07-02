class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # input; nums = array of integers
        # output; product of integers except self
        # read the array to get the product of the integers before the pointed one using 'prod'
        # append that product for each pointer to an empty list called res
        res = []
        prod = 1
        # loop through the array one time to get the product of elements on the left side
        for n in range(len(nums)):
            res.append(prod)
            prod = prod * nums[n]
        # loop through the array again to get the product of elements on the right side by reading in reverse
        # add those products to res by multiplying the values to corresponding matching index to get the final output
        prod = 1
        for n in range(len(nums) - 1, -1, -1): # start, stop, step size
            res[n] = prod * res[n]
            prod = prod * nums[n]
        return res

       