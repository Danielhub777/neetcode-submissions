class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        one = dict()
        for i in nums:
            if i in one:
                one[i]+=1
            else:
                one[i] = 1
        two = sorted(one, key = one.get, reverse = True)
        three = []
        for i in range(0, k):
            three.append(two[i])
        return three
        