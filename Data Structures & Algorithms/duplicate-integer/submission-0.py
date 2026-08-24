class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        one = set(nums)
        if len(one) != len(nums):
            return True
        else:
            return False
        