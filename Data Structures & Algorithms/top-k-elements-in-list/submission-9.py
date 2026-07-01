class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create the freq map for the integers
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1 
        # bucket sort for the freq map
        buccy = [[] for _ in range(len(nums) + 1)]
        for n,c in count.items():
            buccy[c].append(n)
        res = []
        for c in range(len(buccy) -1, 0, -1):
            for n in buccy[c]:
                res.append(n)
                if len(res) == k:
                    return res