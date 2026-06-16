class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, n in enumerate(nums):
            sValue = target - nums[i]
            if sValue in result:
                return [result[sValue], i]
            result[n] = i
        return []