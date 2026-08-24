class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        one = dict()
        for i in range(0,len(nums)):
            if target - nums[i] in one:
                return [one[target-nums[i]], i]
            else:
                one[nums[i]] = i
        