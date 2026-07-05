class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        sorted_map = OrderedDict(sorted(count.items(), reverse=True))    


        for num, feq in sorted_map.items():
            if feq == 1:
                return num
        return -1