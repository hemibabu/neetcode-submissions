class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # input; nums = [---some integers separated by comma---]
        # output; [---k number of most frequent elements---]

        # hashmap for O(1) lookup

        count = {}
        # loop through the input array to create a frequency map of the integers
        for i in nums:
            count[i] = count.get(i,0) + 1 # golden hashmap code

        # bucket sort for sorting the dict
        freq = [[] for _ in range(len(nums) + 1)]
        # unpacking --> accessing and assigning multiple varibales
        for n,c in count.items():
            freq[c].append(n) # append the numbers to bucket based on the freq/count

        res = [] # create empty list to store k elements
        #iterating throught the bucket/frequency from highest value
        for c in range(len(freq) - 1, 0, -1): 
            for n in freq[c]:
                # append any numbers present for the buckets
                res.append(n)
                if len(res) == k:
                    return res