class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {}
        for i in range(len(nums)):
            balance = target - nums[i]
            if balance in sum:
               return [sum[balance], i]
            else:
                sum[nums[i]] = i
        return []