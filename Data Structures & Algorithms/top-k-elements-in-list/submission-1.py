class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        count = {}

        for i in range(len(nums)):
            count[nums[i]]  = count.get(nums[i], 0) + 1
        
        for key, value in count.items():
            bucket[value].append(key)
        res = []

        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res