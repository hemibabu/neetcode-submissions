class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap creation for array of numbers
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1
        # bucket sort empty array creation
        buc_sort = [[] for _ in range(len(nums) + 1)] # for len+1 array buckets
        # append the numbers to the buckets based on their count
        for n,c in count.items():
            buc_sort[c].append(n)
    
        # emplty list creation to store result
        result = []
        # read the bucket in reverse and append k number of n's in the list
        for c in range(len(buc_sort) - 1, 0, -1):
            for n in buc_sort[c]:
                result.append(n)
                if len(result) == k:
                    return result