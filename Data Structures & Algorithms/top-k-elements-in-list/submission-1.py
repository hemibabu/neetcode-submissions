class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1

        bucket_sort = [[] for _ in range(len(nums) + 1)]
        for n,c in count.items():
            bucket_sort[c].append(n)
        result = []
        for c in range(len(bucket_sort) -1, 0, -1):
            for n in bucket_sort[c]:
                result.append(n)
                if len(result) == k:
                    return result