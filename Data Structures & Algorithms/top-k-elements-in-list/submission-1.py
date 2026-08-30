class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        t = []
        for i, g in count.items():
            t.append([g, i])
        t.sort()

        res = []
        while len(res) < k:
            res.append(t.pop()[1])
        return res